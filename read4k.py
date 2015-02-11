class Solution:
    # read n characters from the file
    # two borders: 
    # 1. end of file before n
    # 2. n
    def read(self, buff, n):
        eof = False
        read_count = n/4
        left_count = n%4
        output = ""

        for i in range(read_count):
            if eof is False:
                return output

            self.read4(buff)
            if len(buff) < 4:
                eof = True

            output += buff
            
        if left_count > 0:
            self.read4(buff)
            output += buff[0:min(len(buff),left_count)]
        return output

    # will be called multiple times
    # two borders:
    # 1. eof, n
    # extra buffer save what's left from last call 
    def __init__(self):
        self.last_buff = ""
        self.eof = False

    def read(self, buff, n):
        output = ""
        if len(self.last_buff) > 0:
            output += last_buff[0:min(len(last_buff),n)]
            n -= min(len(last_buff),n)
            last_buff = last_buff[min(len(last_buff),n)+1:]
        read_count = n / 4
        left_count = n % 4
        for i in range(read_count):
            if self.eof:
                return output
            
            self.read(buff)
            if len(buff) < 4:
                eof = True
            output += buff
        
        if left_count > 0 and self.eof is False:
            self.read(buff)
            output += buff[0:min(len(buff),left_count)] 
            self.last_buff = buff[min(len(buff),left_count)+1:] 
            if len(buff) < left_count:
                self.eof = True

        return output
        
        
    


