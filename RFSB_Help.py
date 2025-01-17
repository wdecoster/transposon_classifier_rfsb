############################################################################
##### Transposon Classifier RFSB - part of Transposon Ultimate #############
##### Kevin Riehl (kevin.riehl.de@gmail.com, 2021) #########################
############################################################################

# Methods
def helpExplanations():
    print("Transposon Classifier \"RFSB\" (v1.0, 2021, Kevin Riehl)")
    print("")
    print("USAGE")
    print("  transposon_classifier_RFSB [-help] [-mode]")
    print("")
    print("MODE [1] \"classify\"")
    print("(mandatory):")
    print("  -fastaFile <String>")
    print("    Fasta file containing DNA sequences")
    print("  -outputPredictionFile <String>")
    print("    Output prediction file containing classification results")
    print("(optional):")
    print("  -modelFile <String>")
    print("    File containing model for classification, default: models/TE_Classifier_RFSB_models_ALL_Big.pickle")
    print("  -kmerConfigFile <String>")
    print("    Configuration file containing k-mers, default: config/kmers.txt")
    print("  -proteinDBFile <String>")
    print("    Configuration file containing NCBI CDD PSSM model IDs, default: config/RPSTBLASTN_LIB/db_large.pn")
    print("  -tempFolder <String>")
    print("    Folder in which temporary files are stored to, default: (folder of the outputFile)")
    print("  -deleteTempFiles <String>")
    print("    Whether to delete temporary feature files, default: True")
    print("")
    print("MODE [2] \"evaluate\"")
    print("(mandatory):")
    print("  -predLabelFile <String>")
    print("    File containing predicted labels = classification results/output of MODE [1]")
    print("  -trueLabelFile <String>")
    print("    File containing true labels")
    print("(optional):")
    print("  -printResults <Boolean>")
    print("    Whether to print results into console, default: True")
    print("  -saveResultsCSV <Boolean>")
    print("    Whether to save results as CSV file, default: True")
    print("  -saveResultsPickle <Boolean>")
    print("    Whether to save output as .pickle file, default: False")
    print("  -outputPickleFile <String>")
    print("    Desired Pickle output file containing statistics, default: predLabelFile+\"_results.pickle\"")
    print("  -outputCSVFile <String>")
    print("    Desired CSV output file containing statistics, default: predLabelFile+\"_results.csv\"")
    print("  -generateDiagramPNG <Boolean>")
    print("    Whether to render diagram and save as PNG, default: True")
    print("  -generateDiagramSVG <Boolean>")
    print("    Whether to render diagram and save as SVG, default: True")
    print("  -diagTitle <String>")
    print("    The rendered diagrams' title")
    print("  -outputPNGFile <String>")
    print("    Desired PNG output file for rendered diagram, default: predLabelFile+\"_diagram.png\"")
    print("  -outputSVGFile <String>")
    print("    Desired SVG output file for rendered diagram, default: predLabelFile+\"_diagram.svg\"")
    print("")
    print("MODE [3] \"trainModel\"")
    print("(mandatory):")
    print("  -fastaFile <String>")
    print("    Fasta file containing DNA sequences")
    print("  -labelFile <String>")
    print("    Fasta file containing true class labels")
    print("  -outputModelFile <String>")
    print("    Desired path to store output model")
    print("(optional):")
    print("  -taxonomyConfigFile <String>")
    print("    Configuration file containing the taxonomy scheme used, if not given taxonomy will automatically be generated from labels in labelFile, default: (none)")
    print("  -proteinDBFile <String>")
    print("    Configuration file containing NCBI CDD PSSM model IDs, default: config/RPSTBLASTN_LIB/db_large.pn")
    print("  -kmerConfigFile <String>")
    print("    Configuration file containing k-mers, default: config/kmers.txt")
    print("  -eThreshold <Float>")
    print("    e-Value threshold to consider RPSTBLASTN findings, default: 5.0")
    print("   -tempFolder <String>")
    print("     Folder in which temporary files are stored to, default: (folder of the outputFile)")
    print("  -deleteTempFiles <Boolean>")
    print("    Whether to delete temporary feature files, default: True")
    print("")