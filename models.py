from django.db import models

# Create your models here.

class TweetFile( models.Model ):

    file_name = models.CharField( max_length = 255 )
    export_file_name = models.CharField( max_length = 255, blank = True, null = True )
    date = models.DateTimeField( blank = True, null = True )
    date_range_start = models.DateTimeField( blank = True, null = True )
    date_range_end = models.DateTimeField( blank = True, null = True )
    status = models.CharField( max_length = 255, blank = True, null = True )
    create_date = models.DateTimeField( auto_now_add = True )
    last_update = models.DateTimeField( auto_now = True )


    #----------------------------------------------------------------------
    # instance methods
    #----------------------------------------------------------------------

    def __unicode__( self ):
 
        # return reference
        string_OUT = ''
 
        if ( self.id ):
        
            string_OUT = str( self.id ) + " - "
            
        #-- END check to see if ID --#
                
        string_OUT += self.file_name
        
        return string_OUT

    #-- END method __unicode__() --#

#-- END class TweetFile --#