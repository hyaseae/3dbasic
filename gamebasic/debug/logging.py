from datetime import datetime

class LOG():
    def __init__(self) -> None:
        self.msglist = []
        self.warnlist = []
        self.errlist = []

    def add_msg(self, text) -> None:
        """ adds text to msg list."""
        self.msglist.append(f"msg at {datetime.now()} : {text}")

    def add_warn(self, text) -> None:
            """ INTUITIVE. SO WHTATT"""
            self.warnlist.append(f"warn at {datetime.now()} : {text}")

    def add_err(self, text) -> None:
            """ adds text to err list."""
            self.errlist.append(f"err at {datetime.now()} : {text}")

    def print_by_level(self, msg = True, warn = True, err = True, file_output = False):
        """
        print messages by level
        """
        if file_output:
            with open(f"log-{datetime.now()}.txt", "w") as file:
                if msg:
                    for msg in self.msglist:
                        file.write(msg + "\n")
                if warn:
                    for msg in self.warnlist:
                        file.write(msg + "\n")
                if err:
                    for msg in self.errlist:
                        file.write(msg + "\n")
            return
        
        if msg:
            for msg in self.msglist:
                print(msg)
        if warn:
            for msg in self.warnlist:
                print(msg)
        if err:
            for msg in self.errlist:
                print(msg)
        
        