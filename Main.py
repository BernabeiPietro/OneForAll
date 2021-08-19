import Cutadapt
import Figaro
import PICRUSt2
import fastQC
from ManagerOfPath import ManagerOfPath
from qiime import qiime

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
    # print("Insert lenght to trunc and filter :")
    # trunc = int(input())
    print("classifier path")
    md["classifier"] = str(input())
    print("witch metadata columns to regroup ")
    md["col_met"]=str(input())
    print("amplicon lenght [V4 200,V3-V4 396")  # da chiedere all'inizio
    md["a_l"] = int(input())
    mp=ManagerOfPath(path_write,path_reads,project_name)
    md["primer_trim"]=fastQC.run_fastqc(md,mp)
    trunc=qiime.generate_trunk(md,mp)
    Cutadapt.cutadapt(mp,trunc)
    md["trunc_f"],md["trunc_r"]=Figaro.run_figaro(mp,md)
    qiime.qiime(md,mp)
    PICRUSt2.picrust2(mp)
