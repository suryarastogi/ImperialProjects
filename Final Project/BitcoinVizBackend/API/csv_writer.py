from django.conf import settings
from blockchain_wrapper import Blockchain
import csv

data_dir = settings.DATA_DIR
csv_dir = data_dir + "/CSV/"

# Most recent difficulty levels 413280, 411264, 409248, 407232

class CSV(object):

    @staticmethod
    def write_block(block):
        txs = Blockchain.get_transactions_by_block(block)
        file_name = csv_dir + str(block) + ".csv"
        with open(file_name, 'wb') as csvfile:
            data_writer = csv.writer(csvfile)

            for tx in txs:
                list = [tx.block_height, tx.hash, tx.time, tx.mempool_count, tx.mempool_size, tx.fee, tx.size, tx.fee_per_byte, tx.confirmation_time]
                data_writer.writerow(list)

    @staticmethod
    def write_difficulty(start_block=407232, count=1):
        end_block = start_block + 2016*4

        errors = []
        for i in range(start_block, end_block):
            print(str(start_block) + ":" + str(i) + ":" + str(end_block))
            try:
                CSV.write_block(i)
            except:
                print("Errored: " + str(i))
                errors.append(i)
        return errors

    @staticmethod
    def write_blocks(block_list):
        errors = []
        for block in block_list:
            try:
                CSV.write_block(block)
            except:
                print("Errored: " + str(block))
                errors.append(block)
        return errors



