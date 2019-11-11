from time import sleep
from celery import Celery

app = Celery('celery_stuff', broker='redis://localhost/2')


@app.task
def serve_a_beer():
    print('Getting a delicious beer!')
    sleep(3)
    print("""
          ------------------------------------------------
                   .   *   ..  . *  *
                 *  * @()Ooc()*   o  .
                     (Q@*0CG*O()  ___
                    |\_________/|/ _ \
                    |  |  |  |  | / | |
                    |  |  |  |  | | | |
                    |  |  |  |  | | | |
                    |  |  |  |  | | | |
                    |  |  |  |  | | | |
                    |  |  |  |  | \_| |
                    |  |  |  |  |\___/  
                    |\_|__|__|_/|
                     \_________/
          ------------------------------------------------
          """)
