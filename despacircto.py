####
##DespacIRCto
##Python Based IRC Client/Server Test
##This file: Server
##Author: AegisTK
####

"""This is a comment string"""

####
##To Do:
##Create class: queueorderer (checks timestamps that are valid and orders messages by them.
##Create functions: has_timestamp(string) and is_empty(string), respectively, these check for timestamp within the
##   message being read, and check for content after the timestamp.
##   delete_first_line(file): removes the first line from the queue file.
####

class Server:

    def __init__(self, masterlog, queuelog, queueorderer):
        self.master = file(masterlog, "a")
        self.queue = file(queuelog, "w")
        self.queueorderer = queueorderer

    def verify_queue(self):
        msg_queue = self.queue.readlines()
        for (message in msg_queue):
            ####
            ##Rules:
            ##Message must have a timestamp
            ##Message should not be empty
            ##For messages starting with "/" (commands), different handling will be done.
            ####
            """Simply ignore messages from queue when rules aren't followed."""
            if (has_timestamp(message) == False)
                msg_queue.pop(0)
                delete_first_line(self.queue)
            elif (is_empty(message) == True):
                msg_queue.pop(0)
                delete_first_line(self.queue)
            else:
                """Message -should- be written properly, so add it to order queue.
                Should be assigned to another thread"""
                self.queueorderer.add(message)

                
    def add_to_master(self):
        """Get messages from ordered queue, add them to master, assigned to a different thread"""
        ordered_queue = self.queueorderer.get_queue()
        if (len(ordered_queue) == 0):
            pass
        else:
            for line in ordered_queue:
                self.master.write(line)
                
    def clean_up(self, limit):
        """Make sure file isn't bigger than set limit."""
        while (len(self.master.readlines()) >= limit):
            delete_first_line(self.master)