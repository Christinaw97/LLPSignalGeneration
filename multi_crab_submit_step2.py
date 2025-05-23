if __name__ == '__main__':

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
    config.section_("Data")

    config.Data.inputDBS = 'phys03'
    config.Data.splitting = 'FileBased'

    #For QCD GEN-SIM samples
    #config.Data.inputDBS = 'global'
    #config.Data.splitting = 'LumiBased'
    #config.Data.lumiMask = 'my_lumi_mask_batch5.qcd.json'

    config.Data.unitsPerJob = 1 #when splitting is 'Automatic', this represents jobs target runtime(minimum 180)
    config.Data.publication = True
    config.Data.ignoreLocality = True

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
#Command to get the dictionary from crab log
#cat log5.txt | grep "Output dataset:" | awk '{print $3}' | awk -F'/' '{print "\""$1"/"$2"/"$3"/"$4"\":\"UL18_DR_step2_"$2"_batch1_v1\","}'


#Command to get the dictionary from crab log
#cat log5.txt | grep "Output dataset:" | awk '{print $3}' | awk -F'/' '{print "\""$1"/"$2"/"$3"/"$4"\":\"/store/group/lpclonglived/apresyan/privateProduction/DR/step2/RunII_UL18/"$2"/batch1/v1/\","}'
    campaign = "Summer24"
    config.JobType.psetName = '/uscms_data/d3/christiw/Run3_MDS/private_generation/Summer24/DR/CMSSW_14_0_19/src/LLPSignalGeneration/pset/DR/EXO-RunIII2024Summer24DRPremix_step2_cfg.py'
    dataset_list ={
            "Summer24_HNL_tau_mN_2_ctau_1000": "/Summer24_HNL_tau_mN_2_ctau_1000_GENSIM/lpclonglived-crab_HNL_tau_mN_2_ctau_1000_Summer24_DRstep1_v2-48cd555cdf6be04e2ea7b276952e1164/USER",
            }
    for name,sample in dataset_list.items():
        config.Data.inputDataset = sample
        config.General.requestName = name
        config.Data.outLFNDirBase = f'/store/group/lpclonglived/christiw/privateProduction/Run3{campaign}/DR_step2/'

        config.JobType.numCores = 1
        config.JobType.maxMemoryMB = 3000
        print(config.General.requestName)
        print(config.Data.inputDataset)
        print(config.Data.outLFNDirBase)
        #submit(config)
        p = Process(target=submit, args=(config,))
        p.start()
        p.join()
