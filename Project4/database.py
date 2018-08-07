class Simpledb:
    def __init__(self, filename):
        self.filename = filename
    def __repr__(self):
        return "<Simpledb file" + "='" +  self.filename + "'>"
    def add(self, name, number):
        file = open(self.filename, "a")
        file.write("%s %s \n" %(name,number))
        file.close()

    def find(self, name):
        file = open(self.filename, "r")
        for line in file:
            s = line.strip().split()
            if s[0] == name:
                print(s[1])
                file.close()
                return s[1]

        file.close()
        print("NAME NOT FOUND")

    def find2(self, name):
        file = open(self.filename, "r")
        for line in file:
            s = line.strip().split()
            if s[0] == name:
                file.close()
                return s[1]

        file.close()
        print("NAME NOT FOUND")
                      
    def delete(self, name):
        target = self.find2(name)
        if target != None:
            file = open(self.filename,"r")
            p = file.readlines()
            file.close()
            file = open(self.filename, "w")    
            for line in p:
                if line != target:
                    file.write(line)
            file.close()
        return target
        
    def update(self, name, number):
        target = self.find2(name)
        if target != None:
            file = open(self.filename,"r")
            p = file.readlines()
            file.close()
            file = open(self.filename, "w")    
            for line in p:
                if line != target:
                    file.write(line)
                else:
                    file.write("%s %s \n" %(name, number))
            file.close()
        return target
            
