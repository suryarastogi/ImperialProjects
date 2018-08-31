package proj.sr3213;

import org.gephi.graph.api.GraphController;
import org.gephi.graph.api.GraphModel;
import org.gephi.graph.api.UndirectedGraph;
import org.gephi.io.exporter.api.ExportController;
import org.gephi.io.exporter.preview.PDFExporter;
import org.gephi.io.exporter.spi.CharacterExporter;
import org.gephi.io.exporter.spi.Exporter;
import org.gephi.io.importer.api.Container;
import org.gephi.io.importer.api.EdgeDirectionDefault;
import org.gephi.io.importer.api.ImportController;
import org.gephi.io.processor.plugin.DefaultProcessor;
import org.gephi.layout.plugin.forceAtlas2.ForceAtlas2;
import org.gephi.layout.plugin.forceAtlas2.ForceAtlas2Builder;
import org.gephi.project.api.ProjectController;
import org.gephi.project.api.Workspace;
import org.openide.util.Lookup;

import java.io.*;

public class GephiWrapper {

    //Layout constants:
    private static final Double LAYOUT_SCALE = 400.0;
    private static final Boolean BARNES_HUTT_OPTIMIZE = true;
    private static final Double BARNES_HUT_THETA = 1.2;
    private static final boolean STRONGER_GRAVITY = true;
    private static final Double GRAVITY = 1.0;
    private static final Boolean ADJUST_SIZES = true;
    private static final int LAYOUT_ITERATIONS = 10000;
    private static final Double EDGE_WEIGHT_INFLUENCE = 1.0;
    private static final Integer THREADS_COUNT = 7;


    private Workspace workspace;
    private GraphModel graphModel;
    private UndirectedGraph graph;

    public GephiWrapper(){
        ProjectController pc = Lookup.getDefault().lookup(ProjectController.class);
        pc.newProject();
        workspace = pc.getCurrentWorkspace();
    }

    public void importFile(String msg) throws FileNotFoundException{
        ImportController importController = Lookup.getDefault().lookup(ImportController.class);
        Container container;
        File file = new File(msg);
        container = importController.importFile(file);
        container.getLoader().setEdgeDefault(EdgeDirectionDefault.UNDIRECTED);

        //Append imported data to GraphAPI
        importController.process(container, new DefaultProcessor(), workspace);

        graphModel = Lookup.getDefault().lookup(GraphController.class).getGraphModel();
        graph = graphModel.getUndirectedGraph();
        System.out.println("Nodes: " + graph.getNodeCount());
        System.out.println("Edges: " + graph.getEdgeCount());
    }

    public int getIterations(){
        int iterations_min = 5000;
        int iterations_scaled = 3000*(1000/((1 + graph.getNodeCount()/25) + (graph.getEdgeCount()/25)));
        int iterations = iterations_min + iterations_scaled;
        System.out.println("Scale: "+ iterations_scaled);
        return iterations;
    }

    public void forceAtlas2Layout(int iterations){
        ForceAtlas2 layout = new ForceAtlas2Builder().buildLayout();
        layout.setGraphModel(graphModel);
        layout.initAlgo();
        layout.resetPropertiesValues();
        layout.setAdjustSizes(ADJUST_SIZES);

        layout.setBarnesHutOptimize(BARNES_HUTT_OPTIMIZE);
        layout.setBarnesHutTheta(BARNES_HUT_THETA);

        layout.setStrongGravityMode(STRONGER_GRAVITY);
        layout.setGravity(GRAVITY);

        layout.setEdgeWeightInfluence(EDGE_WEIGHT_INFLUENCE);
        double layout_scale = graph.getNodeCount()/100 + graph.getEdgeCount()/100;

        layout.setScalingRatio(layout_scale);
        layout.setThreadsCount(THREADS_COUNT);

        for (int i = 0; i < iterations && layout.canAlgo(); i++) {
            if (i % 500 == 0)
                System.out.println("Iteration " + i + " of " + iterations);

            layout.goAlgo();
        }
        layout.endAlgo();
        System.out.println("Iterations: " + iterations + " done");
    }

    public String exportGraph(boolean pdf, String outPath, String outFile) throws FileNotFoundException{
        ExportController ec = Lookup.getDefault().lookup(ExportController.class);
        if(pdf){
            PDFExporter pdfExporter = (PDFExporter) ec.getExporter("pdf");
            try{

                String file_name = outFile.substring(0, outFile.lastIndexOf('.'));
                String img_file = outPath + file_name + ".pdf";
                img_file = img_file.replace("home", "Users");

                System.out.println("Exporting: " + img_file);
                ec.exportFile(new File(img_file));
            }
            catch (IOException ex){
                ex.printStackTrace();
            }
        }

        Exporter exporterGraphML = ec.getExporter("graphml");     //Get GraphML exporter
        exporterGraphML.setWorkspace(workspace);
        StringWriter stringWriter = new StringWriter();
        ec.exportWriter(stringWriter, (CharacterExporter) exporterGraphML);

        outFile = outPath + outFile;

        outFile = outFile.replace("home", "Users");
        System.out.println("Writing out for colouring: " + outFile);

        PrintWriter out = new PrintWriter(outFile);
        out.println(stringWriter.toString());
        out.close();

        return outFile;
    }
}
