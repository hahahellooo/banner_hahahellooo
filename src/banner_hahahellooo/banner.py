from pyfiglet import Figlet
import random
def show():
    f = Figlet(font='slant')
    print(f.renderText('hahahellooo'))


def pic():
    p = """





                                  @@@@@@@@                @@@@@@@
                                @@       @@             @@@     @@@
                               @@        @@@           @@@        @@
                               @@         @@           @@         @@
                              @@@         @@@@@@@@@@@@@@@         @@
                              @@@                                 @@
                              @@@                                  @@
                              @@                                   @@
                              @@                                   @@@
                             @@@       @@@                          @@
                             @@         @               @@@         @@@
                            @@@                                      @@
                            @@@          @@@@@@@@@@@@@@              @@@
                            @@       @@@@@@@@@@@@@@@@@@@@@@@          @@
                           @@@      @@@@ @@@@@@@@@@@@@@@@@@@@          @@
                          @@@       @@ @@@ @@@  @@ @@@ @@@@ @           @@
                         @@@@      @@@       @@@@@@@@@@@@@@@@@           @@
                        @@ @@      @@@     @@@             @@@            @@
                       @@@ @@       @@   @@@                @@            @@@
                       @@  @        @@  @@                @@@              @@@
                      @@  @@         @@@@               @@@@                @@
                     @@@  @@           @@              @@@@                 @@@
                     @@   @@          @@               @@                    @@
                     @@   @@          @@               @@                    @@
                     @@   @@          @@              @@@                    @@
                     @@   @           @@              @@                     @@
                     @@@  @            @@            @@             @@      @@@
                      @@@ @@            @@@        @@@              @@@@  @@@@
                        @@@@              @@@@@@@@@@                   @@@@
                          @@                                            @
                          @@                                            @
                           @                                           @@
                           @@                                          @@
                           @@                                          @@
                           @@                                          @@
                           @@@            @@@@@@@@@@@@@@              @@@
                            @@              @@@@@@@@@@@@@             @@@
                            @@@              @@@      @@@             @@
                             @@@             @@        @@            @@@
                              @@            @@         @@@          @@@
                               @@@@      @@@@           @@@@       @@@
                                  @@@@@@@@                 @@@@@@@@@


                                                                                                    """
                                                                                                    print(p)


def lotto():

    lotto = random.sample(range(1,46),6)
    print(lotto)
