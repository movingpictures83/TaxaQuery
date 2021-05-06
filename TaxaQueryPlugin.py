import PyPluMA

class TaxaQueryPlugin:
    def input(self, filename):
      self.parameters = dict()
      paramfile = open(filename, 'r')

      self.inputfile = open(PyPluMA.prefix()+"/"+paramfile.readline().strip(), 'r')

      self.targets = []
      for line in paramfile:
         self.targets.append(line.strip())

    def run(self):
      self.bacteria = self.inputfile.readline().strip()
      self.bacteria = self.bacteria.split(',')
      self.bacteria = self.bacteria[1:]

    def output(self, filename):
        outfile = open(filename, 'w')
        outfile.write("\"Sample\",\"TotalOTU\",\"Halomonas\",\"Percent Halomonas\"\n")
        for firstline in self.inputfile:
         firstline = firstline.strip()
         #firstline = self.inputfile.readline().strip()
         abundances = firstline.split(',')
         sample = abundances[0]
         abundances = abundances[1:]

         n = len(self.bacteria)
         listabund = dict()
         count = 0
         for i in range(0, n):
            bac = self.bacteria[i]
            bac = bac[:bac.rindex('.')]
            if (int(abundances[i]) != 0):
                if (bac not in listabund):
                    listabund[bac] = int(abundances[i])
                else:
                    listabund[bac] += int(abundances[i])
            count += int(abundances[i])

         #print(listabund)
         #listabund.sort()
         #listabund.reverse()
         #print(listabund)
         abunds = []
         for key in listabund:
            abunds.append((listabund[key], key))
         abunds.sort()
         abunds.reverse()

         #print(abunds)
         countHalo = 0
         for i in range(0, len(abunds)):
            for target in self.targets:
             if (target in abunds[i][1]):
               countHalo += int(abunds[i][0])
               break

         outfile.write(sample+","+str(countHalo)+","+str(count)+","+str(countHalo/float(count)*100)+"\n")
