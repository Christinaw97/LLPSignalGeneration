# Summer 24 Production

got configuration for pset from: https://cms-pdmv-prod.web.cern.ch/mcm/requests?dataset_name=GluGluH-Hto2Sto4B_Par-ctauS-0p1-MH-125-MS-15_TuneCP5_13p6TeV_powheg-pythia8&page=0&shown=2099327



Use `CMSSW_14_0_19`:

### GEN-SIM 
Run `cmsRun pset/GENSIM/EXO-RunIII2024Summer24wmLHEGS-00259_1_cfg.py`

* grid packs is not on cvmfs and on xrootd path
* had to change script line in pset file to : `scriptName = cms.FileInPath('GeneratorInterface/LHEInterface/data/run_generic_tarball_xrootd.sh')`

### DR step 1 + 2
```bash
## step 1
cmsRun pset/DR/EXO-RunIII2024Summer24DRPremix_step1_cfg.py

## step 2
cmsRun pset/DR/EXO-RunIII2024Summer24DRPremix_step2_cfg.py
```


### MDSNano production with nanoAOD v15

```bash
cmsrel CMSSW_15_0_2
cd CMSSW_15_0_2/src
eval `scram runtime -sh`
scram b
git cms-addpkg PhysicsTools/NanoAOD
git clone git@github.com:cms-lpc-llp/HMTntuple.git
```

#### Modify the nanoaod package to add rechits with MDSNano

Cherry pick or change by hand the two commits here, then `scram b`:
* https://github.com/kakwok/cmssw/commit/83bc8aa57b34914a8ce946d45e53ed5777242d92
* https://github.com/kakwok/cmssw/commit/6887978f3dfbc38d1fca979c3ccf4ef520ebbd3a

To Cherry pick, run the following command:

```bash
git remote add kakwok git@github.com:kakwok/cmssw.git
git fetch kakwok # this step might take a while 
# cherry pick the commits, need to resolve conflicts (always keep the version in CMSSW_15_0_2)
git cherry-pick 83bc8aa57b34914a8ce946d45e53ed5777242d92
git cherry-pick 6887978f3dfbc38d1fca979c3ccf4ef520ebbd3a
scram b 
```

then run the following to on AOD files for MINI+NANO v15 step:

`cmsRun pset/MDSNANO/EXO-RunIII2024Summer24NanoAODv15_cfg.py`


The pset is obtained with the following command with modification to add rechits in nanoAOD:

`cmsDriver.py --eventcontent NANOAODSIM --customise Configuration/DataProcessing/Utils.addMonitoring --datatier NANOAODSIM --conditions 150X_mcRun3_2024_realistic_v2 --step PAT,NANO --geometry DB:Extended --scenario pp --era Run3_2024 --python_filename EXO-RunIII2024Summer24NanoAODv15-00307_1_cfg.py --fileout file:EXO-RunIII2024Summer24NanoAODv15-00307.root --number 10 --number_out 10 --no_exec --mc`




# Summer22EE Production

`CMSSW_12_4_11_patch3`: GENSIM, DR step 1 and 2
`CMSSW_13_0_13`: MINI + MDSNANO step
