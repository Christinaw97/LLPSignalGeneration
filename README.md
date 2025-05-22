# Summer 24 Production

got configuration for pset from: [https://cms-pdmv-prod.web.cern.ch/mcm/public/restapi/requests/get_test/EXO-RunIII2024Summer24wmLHEGS-00259](https://cms-pdmv-prod.web.cern.ch/mcm/requests?dataset_name=GluGluH-Hto2Sto4B_Par-ctauS-0p1-MH-125-MS-15_TuneCP5_13p6TeV_powheg-pythia8&page=0&shown=2175)

### GEN-SIM 
Run `cmsRun pset/EXO-RunIII2024Summer24wmLHEGS-00259_1_cfg.py`

* grid packs is not on cvmfs and on xrootd path
* had to change script line in pset file to : `scriptName = cms.FileInPath('GeneratorInterface/LHEInterface/data/run_generic_tarball_xrootd.sh')`

### DR step 1
`cmsRun pset/EXO-RunIII2024Summer24DRPremix_1_cfg.py`

### DR step 2
`cmsRun pset/EXO-RunIII2024Summer24DRPremix_2_cfg.py`

