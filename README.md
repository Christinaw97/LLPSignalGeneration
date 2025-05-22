# Summer 24 HNL Production

got code from: https://cms-pdmv-prod.web.cern.ch/mcm/public/restapi/requests/get_test/EXO-RunIII2024Summer24wmLHEGS-00259

### GEN-SIM 
cmsDriver.py Configuration/GenProduction/python/hnl_genfragment.py --era Run3_2024 --customise Configuration/DataProcessing/Utils.addMonitoring --beamspot DBrealistic --step LHE,GEN,SIM --geometry DB:Extended --conditions 140X_mcRun3_2024_realistic_v26 --customise_commands process.RandomNumberGeneratorService.externalLHEProducer.initialSeed="int(1)"\\nprocess.source.numberEventsInLuminosityBlock="cms.untracked.uint32(100)" --datatier GEN-SIM --eventcontent RAWSIM --python_filename EXO-RunIII2024Summer24wmLHEGS-00259_1_cfg.py --fileout file:EXO-RunIII2024Summer24wmLHEGS-00259.root --number 10 --no_exec --mc

* grid packs is not on cvmfs and on xrootd path
* had to change script line to : `scriptName = cms.FileInPath('GeneratorInterface/LHEInterface/data/run_generic_tarball_xrootd.sh')`
### DR step 1
cmsDriver.py  --era Run3_2024 --customise Configuration/DataProcessing/Utils.addMonitoring --procModifiers premix_stage2 --datamix PreMix --step DIGI,DATAMIX,L1,DIGI2RAW,HLT:2024v14 --geometry DB:Extended --conditions 140X_mcRun3_2024_realistic_v26 --datatier GEN-SIM-RAW --eventcontent PREMIXRAW --python_filename EXO-RunIII2024Summer24DRPremix-00049_1_cfg.py --fileout file:EXO-RunIII2024Summer24DRPremix-00049_0.root --filein file:EXO-RunIII2024Summer24wmLHEGS-00259.root --number 100 --number_out 100 --pileup_input "dbs:/Neutrino_E-10_gun/RunIIISummer24PrePremix-Premixlib2024_140X_mcRun3_2024_realistic_v26-v1/PREMIX" --no_exec --mc
