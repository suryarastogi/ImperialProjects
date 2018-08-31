package proj.sr3213;

import info.blockchain.api.APIException;

import java.io.IOException;
import java.nio.file.Path;
import java.nio.file.Paths;

public class App 
{
    private static final boolean DEV_LOCAL = true;

    public static void main( String[] args ) throws APIException, IOException, InterruptedException {
        /*
        BlockExplorer blockExplorer = new BlockExplorer();

        Transaction tx = blockExplorer.getTransaction("df67414652722d38b43dcbcac6927c97626a65bd4e76a2e2787e22948a7c5c47");
        for (Input i : tx.getInputs())
        {
            System.out.println(i.getPreviousOutput().getValue());
        }
        */
        RabbitWrapper rw;
        if(DEV_LOCAL){
            rw = new RabbitWrapper();
        }
        else{
            rw = new RabbitWrapper("146.169.46.186:5672");
        }
        rw.startConsuming();

        while(true) {
            String message = rw.getMessage();
            System.out.println("[.] Layout: " + message);

            //Layout

            Path p = Paths.get(message);
            String out_file = p.getFileName().toString();
            System.out.println("File: " + out_file);
            String out_path = "/home/surya/backend/data/Gephied/";

            GephiWrapper gw = new GephiWrapper();
            gw.importFile(message);
            int iterations = gw.getIterations();

            gw.forceAtlas2Layout(iterations);

            //Export  graph
            out_file = gw.exportGraph(true, out_path, out_file);
            rw.basicPublish(out_file);
        }
    }
}
