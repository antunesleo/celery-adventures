from time import sleep
from celery import Celery

# Creating a celery instance.
app = Celery('first_app', broker='redis://localhost/2')


@app.task
def serve_a_beer():
    """
     This is a celery task. Just a normal function with task decorator.
     Note that we use the decorator from a celery insance.
    """
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
