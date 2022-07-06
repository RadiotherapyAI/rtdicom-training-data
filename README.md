# Training Data

The purpose of the data within this repository is to collate the datasets that
are utilised to build the public Radiotherapy AI models.

## Upstream License Change Note

The HNSCC dataset was downloaded from
<https://wiki.cancerimagingarchive.net/display/Public/HNSCC> in 2021 and
was provided under the Creative Commons Attribution 3.0 Unported (CC BY 3.0)
license. Since downloading the data the license at the original source has
changed to the [TCIA Restricted License Agreement](https://wiki.cancerimagingarchive.net/download/attachments/4556915/TCIA%20Restricted%20License%2020220519.pdf?version=1&modificationDate=1652964581655&api=v2).

## TODO

- [ ] Provide the conversion code from DeepMind's original dataset format to the DICOM
format.
- [ ] Revert to assigning the different observers into different structure
files, as opposed to grouping them together. NOTE: This will result in a
"breaking change" for this dataset.

## References

### TCIA

Clark K, Vendt B, Smith K, Freymann J, Kirby J, Koppel P, Moore S, Phillips S, Maffitt D, Pringle M, Tarbox L, Prior F. The Cancer Imaging Archive (TCIA): Maintaining and Operating a Public Information Repository, Journal of Digital Imaging, Volume 26, Number 6, December, 2013, pp 1045-1057. DOI: [10.1007/s10278-013-9622-7](https://doi.org/10.1007/s10278-013-9622-7)

### 4D-Lung

<https://wiki.cancerimagingarchive.net/display/Public/4D-Lung#212674141d3f10cc8f084cec86132755a57a1d9c>

Hugo, Geoffrey D., Weiss, Elisabeth, Sleeman, William C., Balik, Salim, Keall, Paul J., Lu, Jun, & Williamson, Jeffrey F. (2016). Data from 4D Lung Imaging of NSCLC Patients. The Cancer Imaging Archive. http://doi.org/10.7937/K9/TCIA.2016.ELN8YGLE

Hugo, G. D., Weiss, E., Sleeman, W. C., Balik, S., Keall, P. J., Lu, J. and Williamson, J. F. (2017), A longitudinal four-dimensional computed tomography and cone beam computed tomography dataset for image-guided radiation therapy research in lung cancer. Med. Phys., 44: 762-771. doi:[10.1002/mp.12059](https://doi.org/10.1002/mp.12059)

S. Balik et al., "Evaluation of 4-Dimensional Computed Tomography to 4-Dimensional Cone-Beam Computed Tomography Deformable Image Registration for Lung Cancer Adaptive Radiation Therapy." Int. J. Radiat. Oncol. Biol. Phys. 86, 372-9 (2013) PMCID: [PMC3647023](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3647023/).

N.O. Roman, W. Shepherd, N. Mukhopadhyay, G.D. Hugo, and E. Weiss, "Interfractional Positional Variability of Fiducial Markers and Primary Tumors in Locally Advanced Non-Small-Cell Lung Cancer during Audiovisual Biofeedback Radiotherapy." Int. J. Radiat. Oncol. Biol. Phys. 83, 1566-72 (2012). DOI:[10.1016/j.ijrobp.2011.10.051](https://doi.org/10.1016/j.ijrobp.2011.10.051)

### DeepMind

<https://github.com/deepmind/tcia-ct-scan-dataset>

S. Nikolov, S. Blackwell, R. Mendes, J. De Fauw, C. Meyer, C. Hughes, H. Askham, B. Romera-Paredes, A. Karthikesalingam, C. Chu, D. Carnell, C. Boon, D. D'Souza, S. A. Moinuddin, K. Sullivan, DeepMind Radiographer Consortium, H. Montgomery, G. Rees, R. Sharma, M. Suleyman, T. Back, J. R. Ledsam, O. Ronneberger, "Deep learning to achieve clinically applicable segmentation of head and neck anatomy for radiotherapy," 2018. Available: https://arxiv.org/abs/1809.04430

W. R.  Bosch,  W.  L.  Straube,  J.  W.  Matthews,  and  J.  A.  Purdy,  "Head-neck  cetuximab  -  the cancer  imaging  archive,"  2015.  Available:   https://wiki.cancerimagingarchive.net/display/Public/Head-Neck+Cetuximab

C. L. Brouwer,  R. J. H. M. Steenbakkers,  J. Bourhis,  W. Budach,  C. Grau,  V. Grégoire,  M. vanHerk,  A.  Lee,  P.  Maingon,  C.  Nutting,  B.  O'Sullivan,  S.  V.  Porceddu,  D.  I.  Rosenthal,  N.  M.Sijtsema,  and  J.  A.  Langendijk,  "CT-based  delineation  of  organs  at  risk  in  the  head  and  neck region:   DAHANCA,  EORTC,  GORTEC,  HKNPCSG,  NCIC  CTG,  NCRI,  NRG  oncology  andTROG consensus guidelines," Radiother. Oncol., vol. 117, no. 1, pp. 83-90, Oct. 2015. Available: http://dx.doi.org/10.1016/j.radonc.2015.07.041

M. L. Zuley, R. Jarosz, S. Kirk, L. Y., R. Colen, K. Garcia, and N. D. Aredes, "Radiology data from the  cancer  genome  atlas  head-neck  squamous  cell  carcinoma  [TCGA-HNSC]  collection,"  2016. Available: http://dx.doi.org/10.7937/K9/TCIA.2016.LXKQ47MS

### Soft-tissue-Sarcoma

<https://wiki.cancerimagingarchive.net/display/Public/Soft-tissue-Sarcoma#21266533c87a799b615349f8bae03eb6495ce094>

Vallières, Martin, Freeman, Carolyn R., Skamene, Sonia R., & El Naqa, Issam. (2015). A radiomics model from joint FDG-PET and MRI texture features for the prediction of lung metastases in soft-tissue sarcomas of the extremities. The Cancer Imaging Archive. http://doi.org/10.7937/K9/TCIA.2015.7GO2GSKS

Vallières, M., Freeman, C. R., Skamene, S. R., & Naqa, I. El. (2015, June 29). A radiomics model from joint FDG-PET and MRI texture features for the prediction of lung metastases in soft-tissue sarcomas of the extremities. Physics in Medicine and Biology. IOP Publishing. http://doi.org/10.1088/0031-9155/60/14/5471

### LCTSC

<https://wiki.cancerimagingarchive.net/display/Public/Lung+CT+Segmentation+Challenge+2017#24284539021ca3c9a0724b0d9df784f1699d35e2>

Yang, Jinzhong; Sharp, Greg; Veeraraghavan, Harini ; van Elmpt, Wouter ; Dekker, Andre; Lustberg, Tim; Gooding, Mark. (2017). Data from Lung CT Segmentation Challenge. The Cancer Imaging Archive. http://doi.org/10.7937/K9/TCIA.2017.3r3fvz08

Yang, J. , Veeraraghavan, H. , Armato, S. G., Farahani, K. , Kirby, J. S., Kalpathy‐Kramer, J. , van Elmpt, W. , Dekker, A. , Han, X. , Feng, X. , Aljabar, P. , Oliveira, B. , van der Heyden, B. , Zamdborg, L. , Lam, D. , Gooding, M. and Sharp, G. C. (2018), Autosegmentation for thoracic radiation treatment planning: A grand challenge at AAPM 2017. Med. Phys.. . doi: [10.1002/mp.13141](https://doi.org/10.1002/mp.13141)

### Pediatric-CT-SEG

<https://wiki.cancerimagingarchive.net/pages/viewpage.action?pageId=89096588#89096588bcab02c187174a288dbcbf95d26179e8>

Jordan, P., Adamson, P. M., Bhattbhatt, V., Beriwal, S., Shen, S., Radermecker, O., Bose, S., Strain, L. S., Offe, M., Fraley, D., Principi, S., Ye, D. H., Wang, A. S., Van Heteren, J., Vo, N.-J., & Schmidt, T. G. (2021). Pediatric Chest/Abdomen/Pelvic CT Exams with Expert Organ Contours (Pediatric-CT-SEG) (Version 2) [Data set]. The Cancer Imaging Archive. https://doi.org/10.7937/TCIA.X0H0-1706

Jordan, P., Adamson, P. M., Bhattbhatt, V., Beriwal, S., Shen, S., Radermecker, O., Bose, S., Strain, L. S., Offe, M., Fraley, D., Principi, S., Ye, D. H., Wang, A. S., Heteren, J., Vo, N., & Schmidt, T. G. (2022). Pediatric chest‐abdomen‐pelvis and abdomen‐pelvis CT images with expert organ contours. In Medical Physics (Vol. 49, Issue 5, pp. 3523-3528). Wiley. https://doi.org/10.1002/mp.15485

### HNSCC

<https://wiki.cancerimagingarchive.net/display/Public/HNSCC>

Grossberg A, Elhalawani H, Mohamed A, Mulder S, Williams B, White AL, Zafereo J, Wong AJ, Berends JE, AboHashem S, Aymard JM, Kanwar A, Perni S, Rock CD, Chamchod S, Kantor M, Browne T, Hutcheson K, Gunn GB, Frank SJ, Rosenthal DI, Garden AS, Fuller CD, M.D. Anderson Cancer Center Head and Neck Quantitative Imaging Working Group. (2020) HNSCC [ Dataset ]. The Cancer Imaging Archive. DOI: https://doi.org/10.7937/k9/tcia.2020.a8sh-7363

Grossberg  A, Mohamed A, Elhalawani H, Bennett W, Smith K, Nolan T,  Williams B, Chamchod S, Heukelom J, Kantor M, Browne T, Hutcheson K, Gunn G, Garden A, Morrison W, Frank S, Rosenthal D, Freymann J, Fuller C. (2018) Imaging and Clinical Data Archive for Head and Neck Squamous Cell Carcinoma Patients Treated with Radiotherapy. Scientific Data 5:180173 (2018) DOI: [10.1038/sdata.2018.173](https://doi.org/10.1038/sdata.2018.173)

Elhalawani, H., Mohamed, A., White, A. et al. Matched computed tomography segmentation and demographic data for oropharyngeal cancer radiomics challenges. Sci Data 4, 170077 (2017). DOI: [10.1038/sdata.2017.77](https://doi.org/10.1038/sdata.2017.77)
