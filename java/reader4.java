public class read4 extends Reader4 {
    
    /*
 *    @param buf  Destination buffer
 *    @param n    Maximum number of characters to read
 *    @return     The number of characters read
 * */

    public int read(char[] buf, int n) {
        //
        char[] buffer = new char[4];
        int readBytes = 0;
        boolean eof = false;

        // When file not ended, and not reached file limit. 
        while (!eof && readBytes < n) {
            // read content into buffer and record buffer size
            int sz = read4(buffer);
            if (sz < 4) eof = true;
            // size that is actually useful
            int bytes = Math.min(n - readBytes, sz);
            // read content from buffer to buf, starting from readBytes, 
            System.arraycopy(buffer, 0, buf, readBytes, bytes);
            // extends 
            readBytes += bytes;
        }

        return readBytes;
    }

    // buffer to store chars for next read
    private char[] buffer = new char[4];
    int offset = 0, bufsize = 0;
    
/*
 *  @param buf   Destination buffer
 *  @param n     Maximum number of characters to read
 *  @return      The number of characters read
 *  This is a very hard coding question
 *  Important flags: 
 *  1. eof: end of file flag. 
 *  2. readBytes: determine if required amount of content has been read
 *  3. bufsize: store the left over size
 *  4. bytes: stores the actual read content size
 *  5. offset: in case when there are left over in the buffer.
 * */
    public int readII(char[] buf, int n) {
        int readBytes = 0;
        boolean eof = false;
        // determine if reached eof, or if surpassed buffer size upper limit.
        while (!eof && readBytes < n) {
            // check buffer size, if buffer size is 0, read buffer, if not, means something still there from last time.
            int sz = (bufsize > 0) ? bufsize : read4(buffer);
            // if bufsize == 0: nothing to read from buffer, sz < 4, end of file reached.
            if (bufsize == 0 && sz < 4) eof = true;
            // determine the number of bytes to read
            int bytes = Math.min(n - readBytes, sz);
            // read from buffer to buf, starting from offset, and read the number of bytes
            // from 
            System.arraycopy(buffer /* src */, offset /* srcPos */,
               buf /* dest */, readBytes /* destPos */, bytes /* length */);

            // reset offset
            offset = (offset + bytes) % 4;
            bufsize = sz - bytes;
            readBytes += bytes;
        }
        return readBytes;
    }
}
