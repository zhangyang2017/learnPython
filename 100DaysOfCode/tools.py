from typing import Dict
import sys

sys.stdout.write("\033[1;36m")

class Seq_tool_sets:
    """
    this class has a few tools for sequencing analysis
    """
    def __init__(self, seq_file_name: str) -> None:
        self.seq = seq_file_name
        self.seq_dict: Dict = {}

        seq_fhandle = open(self.seq)

        for line in seq_fhandle:
            line = line.strip("\n")
            if line.startswith(">"):
                header = line
                self.seq_dict[header] = ""
            else:
                self.seq_dict[header] += line

        seq_fhandle.close()

#################
## method 1
#################

    def count_seqs(self):
        """this method counts how many sequence entries are in a multi-fasta file

        :return: number of records
        """
        seq_records = len(self.seq_dict)
        return seq_records

#################
## method 2
#################

    def seq_length(self):
        """
        this function takes a fasta file as input, then count length for each sequence
        :return: number
        """
        length_dict = {}
        for key, value in self.seq_dict.items():
            length_dict[key] = len(value)

        sequence_lengths = length_dict.values()
        max_length = max(sequence_lengths)
        min_length = min(sequence_lengths)
        avg_length = sum(sequence_lengths) / len(self.seq_dict)

        max_id = [item for item in length_dict
                  if length_dict[item] == max_length]
        min_id = [item for item in length_dict
                  if length_dict[item] == min_length]

        return [max_length, min_length, avg_length, max_id, min_id]

#################
## method 3
#################

    def summary(self):
        """this function returns stat summary for the fasta file"""
        seq_length = self.count_seqs()
        stat = self.seq_length()

        print("Here is a brief summary of the fasta file " + self.seq + ": \n"
              "1. there are a total of " + str(seq_length) + " sequences;" + "\n"
              "2. average length is " + str(int(stat[2])) + " bases;" + "\n"
              "3. " + str(stat[3][0][1:]) + " has the longest sequence of " + str(stat[0]) + " bases;" + "\n"
              "4. " + str(stat[4][0][1:]) + " has the shortest sequence of " + str(stat[1]) + " bases.")
        return None

##### testing ######

test: Seq_tool_sets = Seq_tool_sets("T10000.pep")
test.summary()
sys.stdout.write("\033[0m")
