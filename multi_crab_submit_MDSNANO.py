if __name__ == '__main__':
    import os
    from CRABAPI.RawCommand import crabCommand
    from CRABClient.ClientExceptions import ClientException
    from multiprocessing import Process
    #from httplib import HTTPException

    #from CRABClient.UserUtilities import config
    #config = config()
    from WMCore.Configuration import Configuration
    config = Configuration()

    config.section_("General")
    config.General.workArea = 'crab'
    config.General.transferOutputs = True
    config.General.transferLogs = False

    config.section_("JobType")
    config.JobType.pluginName = 'Analysis'
    config.JobType.psetName = f'{os.environ["CMSSW_BASE"]}/src/LLPSignalGeneration/pset/MDSNANO/EXO-RunIII2024Summer24NanoAODv15_cfg.py'
    config.section_("Data")
    config.Data.inputDBS = 'global'
    config.Data.splitting = 'FileBased'

    config.Data.unitsPerJob = 1 #when splitting is 'Automatic', this represents jobs target runtime(minimum 180)
    config.Data.publication = True
    config.Data.ignoreLocality = True
    config.Data.allowNonValidInputDataset = True
    config.section_("Site")
    config.Site.storageSite = 'T3_US_FNALLPC'
    config.Site.whitelist = ['T2_US_*','T3_US_FNALLPC']
    config.Site.ignoreGlobalBlacklist = True
    
    def submit(config):
        try:
            crabCommand('submit', config = config)
        except ClientException as cle:
            print("Failed submitting task: %s" % (cle))

    #############################################################################################
    ## From now on that's what users should modify: this is the a-la-CRAB2 configuration part. ##
    #############################################################################################
    dataset_list =[

        '/Summer24_HNL_tau_mN_2_ctau_1000_GENSIM/lpclonglived-crab_Summer24_HNL_tau_mN_2_ctau_1000_v2-89578c67bc58e175e14cb8efc9d9e047/USER',
]
    for sample in dataset_list:
        name = sample.split('/')[1]
        print(name)
        config.Data.inputDataset = sample 
        config.General.requestName = name
        config.Data.outLFNDirBase = f'/store/group/lpclonglived/displacedJetMuonNtuple/MDSNano/Run3Summer24/v2/'
        os.system(f"rm -rf crab/crab_{name}")
        config.JobType.numCores = 1
        config.JobType.maxMemoryMB = 2500
        print(config.General.requestName)
        print(config.Data.inputDataset)
        print(config.Data.outLFNDirBase)
        #submit(config)
        p = Process(target=submit, args=(config,))
        p.start()
        p.join()
