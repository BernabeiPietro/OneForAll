import Cutadapt
import Figaro
import Meta_Create
import PICRUSt2_Tot
import QIIME2_body
import QIIME2_import
import QIIME2_tail
import Save_condition
import dim_min_sample_finder

import open_qza_to_PICRUSt2
import tools_for_raw
from ManagerOfPath import ManagerOfPath

if __name__ == '__main__':
    md = {}
    # esiste un cond_file? se si usa quello (da scriverlo)

    path_reads = str(input(print("Insert path of raw reads (250bp) to reads.zip"))) #un conto è il path dello zip da cui estrarre le reads e uno è il path della cartella generata.
    path_write = str(input(print("Insert path to write with '/' ")))
    project_name = str(input(print("nome progetto (no_space):")))

    mp = ManagerOfPath(path_write, path_reads, project_name)

    md["path_reads"] = path_reads
    md["path_write"] = path_write
    md["project_name"] = project_name


    md["seq_ampstr"] = str(input(print("sequenza amplificata?")))
    md["tread"] = str(input(print("N of treads? (max 16)")))
    md["classifier"] = str(input(print("classifier path")))
    print("Insert metadata column to group data in weighted unifrac :")
    md["col_met"] = str(input() or "0")  # potrebbero essere più di una e per ognuna andrebbe corso il comando: "qiime diversity beta-group-significance" in QIIME2_tail.py

    print("amplicon lenght [V4-V5 372]")  # da chiedere all'inizio http://omegabioservices.com/index.php/16s-reference/
    md["a_l"] =372#str(input())
    md["primer_forward_l"] = 19
    md["primer_reverse_l"] = 20

    Save_condition.save_cond_md(md, mp)
    #   Save_condition.save_cond_mp(mp)

    # ############ inizia da qua il programma ############

    #estraggo e importo il nome delle reads nella cartella giusta
    tools_for_raw.extract_raw(mp)
    tools_for_raw.rename(mp)
    tools_for_raw.take_barcode(mp, md)

    # genero il file qzv
    QIIME2_import.q_import(mp)

    Cutadapt.cutadapt(mp, md)
    md["trunc_f"], md["trunc_r"] = Figaro.run_figaro(mp, md)
    QIIME2_import.q_import(mp)
    Meta_Create.metadata(mp)
    md["metadata"] = str(input(print("where is metadata")))
    QIIME2_body.qiime_body(md, mp)
    md["dim_min_sample"] = dim_min_sample_finder.dim_min_sample(mp, md)
    QIIME2_tail.q_tail(md, mp)
    open_qza_to_PICRUSt2.open_qza_to_picrust_tot(mp)
    PICRUSt2_Tot.picrust2_tot(mp)
    PICRUSt2_Tot.from_ec_to_KO_tot(mp)

    print("Ho finito, felice di servirti!")
