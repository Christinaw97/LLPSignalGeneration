if __name__ == '__main__':

    #filter efficiency

    from CRABAPI.RawCommand import crabCommand
    from CRABClient.ClientExceptions import ClientException
    #from httplib import HTTPException

    from multiprocessing import Process
    from WMCore.Configuration import Configuration
    config = Configuration()

    config.section_("General")
    config.General.workArea = 'crab'
    config.General.transferOutputs = True
    config.General.transferLogs = False

    config.section_("JobType")
    config.JobType.pluginName = 'PrivateMC'

    config.section_("Data")
    config.Data.inputDBS = 'global'
    config.Data.splitting = 'EventBased'
    config.Data.unitsPerJob = 200 
    config.Data.totalUnits = 1000000 
    #config.Data.totalUnits = 2000 
    #config.Data.totalUnits = 2200000 
    #config.Data.totalUnits = 400000 
    config.Data.publication = True

    config.section_("Site")
    config.Site.storageSite = 'T3_US_FNALLPC'

    # We want to put all the CRAB project directories from the tasks we submit here into one common directory.
    # That's why we need to set this parameter (here or above in the configuration file, it does not matter, we will not overwrite it).

    def submit(config):
        try:
            crabCommand('submit', config = config)
        #except HTTPException as hte:
        #    print ("Failed submitting task: %s" % (hte.headers))
        except ClientException as cle:
            print ("Failed submitting task: %s" % (cle))

    #############################################################################################
    ## From now on that's what users should modify: this is the a-la-CRAB2 configuration part. ##
    #############################################################################################

    batch = "batch2"
    pset_dir = "/uscms/home/christiw/nobackup/Run3_MDS/private_generation/Summer24/GEN-SIM/CMSSW_14_0_19/src/"
    
    config.General.requestName = f'Summer24_HNL_tau_mN_2_ctau_1000'
    config.Data.outputPrimaryDataset = f"HNL_tau_mN_2_ctau_1000"
    config.Data.outLFNDirBase = f'/store/group/lpclonglived/christiw/privateProduction/Run3Summer24/GENSIM/'
    config.JobType.psetName = f"{pset_dir}/EXO-RunIII2024Summer24wmLHEGS-00259_1_cfg.py"
    config.JobType.numCores = 1
    print ('config %s' %(config.JobType.psetName))
    print ('output %s' %(config.Data.outLFNDirBase))
    #submit(config)
    p = Process(target=submit, args=(config,))
    p.start()
    p.join()
