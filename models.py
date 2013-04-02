# django imports
from django.db import models

# base python imports
import os

# tweetnet imports
from tweetnet.models import Tweet

# Create your models here.

class TweetFile( models.Model ):

    #----------------------------------------------------------------------
    # Constants-ish
    #----------------------------------------------------------------------
 
    STATUS_SUCCESS = "Success!"
    STATUS_ERROR_PREFIX = "ERROR - "
    
    # field names
    FIELD_NAME_ID = "ID"
    FIELD_NAME_USER = "User"
    FIELD_NAME_USER_ID = "UserID"
    FIELD_NAME_TEXT = "Text"
    FIELD_NAME_TIME = "Time"
    FIELD_NAME_LANGUAGE = "Language"
    FIELD_NAME_COORDINATES = "Coordinates"
    FIELD_NAME_USER_LOCATION = "UserLocation"
    FIELD_NAME_RETWEET_ID = "RetweetID"
    FIELD_NAME_RETWEET_USER = "RetweetUser"
    FIELD_NAME_URL = "URL"
    FIELD_NAME_HT = "HT"
    
    # field name list
    FIELD_NAME_LIST = []
    FIELD_NAME_LIST.append( TweetFile.FIELD_NAME_ID ) # = "ID"
    FIELD_NAME_LIST.append( TweetFile.FIELD_NAME_USER ) # = "User"
    FIELD_NAME_LIST.append( TweetFile.FIELD_NAME_USER_ID ) # = "UserID"
    FIELD_NAME_LIST.append( TweetFile.FIELD_NAME_TEXT ) # = "Text"
    FIELD_NAME_LIST.append( TweetFile.FIELD_NAME_TIME ) # = "Time"
    FIELD_NAME_LIST.append( TweetFile.FIELD_NAME_LANGUAGE ) # = "Language"
    FIELD_NAME_LIST.append( TweetFile.FIELD_NAME_COORDINATES ) # = "Coordinates"
    FIELD_NAME_LIST.append( TweetFile.FIELD_NAME_USER_LOCATION ) # = "UserLocation"
    FIELD_NAME_LIST.append( TweetFile.FIELD_NAME_RETWEET_ID ) # = "RetweetID"
    FIELD_NAME_LIST.append( TweetFile.FIELD_NAME_RETWEET_USER ) # = "RetweetUser"
    FIELD_NAME_LIST.append( TweetFile.FIELD_NAME_URL ) # = "URL"
    FIELD_NAME_LIST.append( TweetFile.FIELD_NAME_HT ) # = "HT"
 
    #----------------------------------------------------------------------
    # model fields
    #----------------------------------------------------------------------

    file_name = models.CharField( max_length = 255 )
    export_file_name = models.CharField( max_length = 255, blank = True, null = True )
    date = models.DateTimeField( blank = True, null = True )
    date_range_start = models.DateTimeField( blank = True, null = True )
    date_range_end = models.DateTimeField( blank = True, null = True )
    status = models.CharField( max_length = 255, blank = True, null = True )
    create_date = models.DateTimeField( auto_now_add = True )
    last_update = models.DateTimeField( auto_now = True )


    #----------------------------------------------------------------------
    # instance variables
    #----------------------------------------------------------------------


    #----------------------------------------------------------------------
    # instance methods
    #----------------------------------------------------------------------


    def parse_file( self, file_path_IN = "", *args, **kwargs ):
        
        '''
        Accepts path to file we want to parse.  Opens it for reading, then
        loops over records, processing each (just saves data to database to
        start).
        
        Preconditions: File must be accessible at the path passed in.
        
        Postconditions: Closes file once we are done parsing it.  Doesn't alter
           file.
        
        Returns status string, "Success!" on success, detailed error message on
           error.
        '''
        
        # return reference
        status_OUT = self.STATUS_SUCCESS
        
        # declare variables
        me = "parse_file"
        my_file = None
        is_new_record = False
        is_empty_line = False
        is_in_text = False
        current_line = ""
        empty_line_counter = 0
        current_record_values = {}
        current_tweet = None
        
        # first, see if we have a file path.
        if ( ( file_path_IN ) and ( file_path_IN != None ) and ( file_path_IN != "" ) ):
            
            # does file exist?
            if ( os.path.isFile( file_path_IN ) == True ):
                
                # file is a file.  Open it.
                try:
                    
                    with open( file_path_IN, "r" ) as my_file:
                    
                        # initialize variables
                        empty_line_counter = 0
                        is_new_record = True
                        is_empty_line = False
                        is_in_text = False
                        current_record_values = {}
                        current_tweet = None

                        # loop over lines in file.
                        for current_line in my_file:
                            
                            # strip white space.
                            current_line = current_line.strip()
                                
                            # check to see if this is an empty line.
                            if ( ( current_line != "" ) or ( ( current_line == "" ) and ( is_in_text == True ) ) ):
                                
                                # this text is not a record delimiter line.
                                
                                # Are we inside the text field?
                                print( "Found either non-empty line, or empty line within a tweet.  Process." )
                                
                                # first, parse on first tab in line.
                                
                                # see if we got anything back.
                                
                                # If so, see if text to left of tab matches any
                                #    of the pre-defined field names.
                                
                                # If yes, then need to deal with text fiel.it maps 
                                
                            else:
                                
                                # empty. Are we inside the tweet's text?
                                if ( is_in_text eq False ):
                                    
                                    # what line are we on?
                                    
                                else:
                                    
                                    # Should never get here.
    
                                # -- END Check to make sure that we aren't inside text field.  --# 
                                
                            #-- END check to see if empty line. --#
                            
                        #-- END loop over lines in file. --#
                    
                    #-- END with file_path_IN --#
                    
                except Exception as e:
                    
                    status_OUT = self.STATUS_ERROR_PREFIX + "In " + me + "(): File \"" + file_path_IN + "\" caused Exception: " + str( e )
                    
                #-- END try...except around file access. --#
                
            else:
                
                status_OUT = self.STATUS_ERROR_PREFIX + "In " + me + "(): File \"" + file_path_IN + "\" is not a file, so can't parse."
                
            #-- END check to see if file exists. --#
            
        else:
            
            status_OUT = self.STATUS_ERROR_PREFIX + "In " + me + "(): No file path passed in, can't parse file."
            
        #-- END check to see if file path passed in. --#
        
        return status_OUT
        
    #-- END method parse_file() --#

    
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