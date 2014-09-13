 
  
  @staticmethod
    def from_list(fields):
        s = ChimeraStats()
        s.qname = fields[0]
        s.tid5p = int(fields[1])
        s.pos5p = int(fields[2])
        s.tid3p = int(fields[3])
        s.pos3p = int(fields[4])
        s.chimera_name = fields[5]
        s.num_spanning_frags = int(fields[6])
        s.num_unambiguous_frags = int(fields[7])
        s.num_uniquely_aligning_frags = int(fields[8])
        s.neg_mismatches = int(fields[9])
        s.isize_prob = float(fields[10])
        return s

    @staticmethod
    def parse(line_iter):
        for line in line_iter:
            fields = line.strip().split('\t')
            yield ChimeraStats.from_list(fields)