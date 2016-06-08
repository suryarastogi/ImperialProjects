from django.conf import settings
from blockchain_wrapper import Blockchain
import csv

data_dir = settings.DATA_DIR
csv_dir = data_dir + "/CSV/"
diff_dir = data_dir + "/Difficulty/"

class CSV(object):

    @staticmethod
    def write_block(block):
        txs = Blockchain.get_transactions_by_block(block)
        file_name = csv_dir + str(block) + ".csv"
        with open(file_name, 'wb') as csvfile:
            data_writer = csv.writer(csvfile)

            for tx in txs:
                list = [tx.block_height, tx.time, tx.mempool_size, tx.fee_per_byte, tx.confirmation_mins]
                data_writer.writerow(list)

    @staticmethod
    def write_difficulty(start_block=411264):
        end_block = start_block + 2016 + 1

        file_name = csv_dir + str(start_block) + "Difficulty.csv"
        with open(file_name, 'wb') as csvfile:
            data_writer = csv.writer(csvfile)

            for i in range(start_block, end_block):
                print("Block: " +str(i))
                txs = Blockchain.get_transactions_by_block(i)
                for tx in txs:
                    list = [tx.block_height, tx.time, tx.mempool_size, tx.fee_per_byte, tx.confirmation_mins]
                    data_writer.writerow(list)

    @staticmethod
    def get_difficulty(start_block=411264):
        end_block = start_block + 2016 + 1

        errors = []
        for i in range(start_block, end_block):
            print(str(start_block) + ":" + str(i) + ":" + str(end_block))
            try:
                CSV.write_block(i)
            except:
                print("Errored: " + str(i))
                errors.append(i)
        return errors