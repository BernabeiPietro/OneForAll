import Cutadapt
import Figaro
import PICRUSt2_Tot
import PICRUSt2_rarefied
import QIIME2_body
import QIIME2_import
import QIIME2_tail
import dim_min_sample_finder
import fastQC
import open_qza_to_PICRUSt2
import trunc_cuta_finder
from ManagerOfPath import ManagerOfPath
from QIIME2_body import qiime_body

if __name__ == '__main__':
    md={}
    print("nome progetto (no_space):")
    project_name=str(input())
    print("sequenza amplificata?")
    md["seq_ampstr"]=str(input())
    print("N of treads? (max 16)")
    md["tread"] = int(input())
    print("where is metadata")
    md["metadata"] = str(input())
    print("Insert path of reads to reads:")
    path_reads = str(input())
    print("Insert path to write whitout" / " ")
    path_write = str(input())
    print("Insert metadata column to group data in weighted unifrac :")
    md["col_met"] = int(input()) #potrebbero essere più di una e per ognuna andrebbe corso il comando: "qiime diversity beta-group-significance" in QIIME2_tail.py
    print("classifier path")
    md["classifier"] = str(input())
    print("witch metadata columns to regroup ")
    md["col_met"]=str(input())
    print("amplicon lenght [V4 200,V3-V4 396]")  # da chiedere all'inizio
    md["a_l"] = int(input())
    raref_option = str(input())
    print("RunPICRUSt2 with rarefied ASV table? Y or N")
    mp=ManagerOfPath(path_write,path_reads,project_name)
    #inizia da qua il programma

    md["primer_lenght"]=fastQC.run_fastqc(md,mp)
    #genero il file qzv
    QIIME2_import.q_import(mp)
    md["trunc_cuta"] =trunc_cuta_finder.trunc_find(mp)
    Cutadapt.cutadapt(mp, md)
    md["trunc_f"], md["trunc_r"] = Figaro.run_figaro(mp, md)
    QIIME2_body.qiime_body(md, mp)
    md["dim_min_sample"]= dim_min_sample_finder.dim_min_sample(mp,md)
    QIIME2_tail.q_tail(md,mp)
    open_qza_to_PICRUSt2.open_qza_to_picrust_tot(mp)
    PICRUSt2_Tot.picrust2_tot(mp)
    PICRUSt2_Tot.from_ec_to_KO_tot(mp)
    if raref_option=="Y":
        open_qza_to_PICRUSt2.open_qza_to_picrust_rarefied(mp)
        PICRUSt2_rarefied.picrust2_tot(mp)
        PICRUSt2_rarefied.from_ec_to_KO_raref(mp)
    print("Ho finito, felice di servirti!")
    condition=open("condition.txt","w")
    condition.write(md)
    condition.close()
