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
    
    # Field name list (now a map)
    #FIELD_NAME_LIST = []
    #FIELD_NAME_LIST.append( TweetFile.FIELD_NAME_ID ) # = "ID"
    #FIELD_NAME_LIST.append( TweetFile.FIELD_NAME_USER ) # = "User"
    #FIELD_NAME_LIST.append( TweetFile.FIELD_NAME_USER_ID ) # = "UserID"
    #FIELD_NAME_LIST.append( TweetFile.FIELD_NAME_TEXT ) # = "Text"
    #FIELD_NAME_LIST.append( TweetFile.FIELD_NAME_TIME ) # = "Time"
    #FIELD_NAME_LIST.append( TweetFile.FIELD_NAME_LANGUAGE ) # = "Language"
    #FIELD_NAME_LIST.append( TweetFile.FIELD_NAME_COORDINATES ) # = "Coordinates"
    #FIELD_NAME_LIST.append( TweetFile.FIELD_NAME_USER_LOCATION ) # = "UserLocation"
    #FIELD_NAME_LIST.append( TweetFile.FIELD_NAME_RETWEET_ID ) # = "RetweetID"
    #FIELD_NAME_LIST.append( TweetFile.FIELD_NAME_RETWEET_USER ) # = "RetweetUser"
    #FIELD_NAME_LIST.append( TweetFile.FIELD_NAME_URL ) # = "URL"
    #FIELD_NAME_LIST.append( TweetFile.FIELD_NAME_HT ) # = "HT"

    # field name to Tweet model field map
    FIELD_NAME_TO_MODEL_FIELD_DICT = {}
    FIELD_NAME_TO_MODEL_FIELD_DICT[ TweetFile.FIELD_NAME_ID ] = "twitter_tweet_id" # = "ID"
    FIELD_NAME_TO_MODEL_FIELD_DICT[ TweetFile.FIELD_NAME_USER ] = "twitter_user_screenname" # = "User"
    FIELD_NAME_TO_MODEL_FIELD_DICT[ TweetFile.FIELD_NAME_USER_ID ] = "twitter_user_twitter_id" # = "UserID"
    FIELD_NAME_TO_MODEL_FIELD_DICT[ TweetFile.FIELD_NAME_TEXT ] = "tweet_text" # = "Text"
    FIELD_NAME_TO_MODEL_FIELD_DICT[ TweetFile.FIELD_NAME_TIME ] = "tweet_timestamp" # = "Time"
    FIELD_NAME_TO_MODEL_FIELD_DICT[ TweetFile.FIELD_NAME_LANGUAGE ] = "tweet_language" # = "Language"
    FIELD_NAME_TO_MODEL_FIELD_DICT[ TweetFile.FIELD_NAME_COORDINATES ] = "tweet_coordinates" # = "Coordinates"
    FIELD_NAME_TO_MODEL_FIELD_DICT[ TweetFile.FIELD_NAME_USER_LOCATION ] = "user_location" # = "UserLocation"
    FIELD_NAME_TO_MODEL_FIELD_DICT[ TweetFile.FIELD_NAME_RETWEET_ID ] = "tweet_retweet_id" # = "RetweetID"
    FIELD_NAME_TO_MODEL_FIELD_DICT[ TweetFile.FIELD_NAME_RETWEET_USER ] = "tweet_retweet_user_twitter_id" # = "RetweetUser"
    FIELD_NAME_TO_MODEL_FIELD_DICT[ TweetFile.FIELD_NAME_URL ] = "twitter_tweet_id" # = "URL"
    FIELD_NAME_TO_MODEL_FIELD_DICT[ TweetFile.FIELD_NAME_HT ] = "twitter_tweet_id" # = "HT"
    
    # field name to model field map
 
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

    
    def create_tweet_instance( self, field_value_dict_IN = None, *args, **kwargs ):
    
        '''
        Accepts dict that maps tweet field names to values.  Creates an
           instance of tweetnet Tweet model, stores values in it, then saves it
           to the database.  Returns status message.
        '''
    
        # return reference
        status_OUT = self.STATUS_SUCCESS
        
        # declare variables
        me = "create_tweet_instance"
        tweet_instance = None
        current_name = ""
        current_value = ""
        current_model_field_name = ""
        
        # first, make sure we have values.
        if ( ( field_value_dict_IN ) and ( field_value_dict_IN != None ) ):
        
            # Create a tweet
            tweet_instance = Tweet()
            
            # place values from map into tweet.
            for current_name, current_value in field_value_dict_IN.items():
            
                # get model field name for the name.
                if ( current_name in self.FIELD_NAME_TO_MODEL_FIELD_DICT ):
                
                    # get model field name for this field.
                    current_model_field_name = self.FIELD_NAME_TO_MODEL_FIELD_DICT[ current_name ]
                    
                else:
                
                    # unknown field name.  Error.
                    current_model_field_name = ""
                    
                #-- END check to see if we have a model field name. --#
                
                # got a model field name?
                if ( ( current_model_field_name ) and ( current_model_field_name != "" ) ):
                
                    # got one.  Set property in model instance.
                    setattr( tweet_instance, current_mode_field_name, current_value )
                
                #-- END check to see where we place current field. --#
                
            #-- END loop over field items passed in. --#
            
            # Special processing?  This is where we'd do special processing based
            #    on field values - get and store length of tweet, parse lat and
            #    long coordinates out of coordinates string, etc.
            # For now, just get this all working.
            
            # save it.
            tweet_instance.save()
            status_OUT = self.STATUS_SUCCESS
            
            # garbage collection?
        
        else:
        
            # ERROR - no values passed in, so can't make instance.
            status_OUT = self.STATUS_ERROR_PREFIX + "no tweet information passed in, so can't create tweet instance."
        
        #-- END check to make sure we have values.
        
        return status_OUT
        
    #-- END method create_tweet_instance() --#


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
        line_counter = -1
        current_line = ""
        empty_line_counter = 0
        current_record_values = {}
        current_field_name = ""
        split_tweet_list = None
        field_name_string = ""
        field_value_string = ""
        is_field_name = False
        last_field_name = ""
        create_status = ""
 
        # first, see if we have a file path.
        if ( ( file_path_IN ) and ( file_path_IN != None ) and ( file_path_IN != "" ) ):
            
            # does file exist?
            if ( os.path.isFile( file_path_IN ) == True ):
                
                # file is a file.  Open it.
                try:
                    
                    with open( file_path_IN, "r" ) as my_file:
                    
                        # initialize variables
                        line_counter = 0
                        empty_line_counter = 0
                        current_record_values = {}
                        current_field_name = ""
                        split_tweet_list = None
                        field_name_string = ""
                        field_value_string = ""
                        is_field_name = False
                        last_field_name = ""

                        # loop over lines in file.
                        for current_line in my_file:
                            
                            # increment line counter
                            line_counter += 1
                            
                            # strip white space?  Yes, for now.
                            current_line = current_line.strip()
                                
                            # check to see if this is an empty line.
                            if ( ( current_line != "" ) or ( ( current_line == "" ) and ( current_field_name == self.FIELD_NAME_TEXT ) ) ):
                                
                                # this text is not a record delimiter line. See
                                #    if it is the first line in a new record.
                                if ( empty_line_counter >= 2 ):
                                
                                    # Looks like this is the first line in a new
                                    #    record.  Create tweet instance from
                                    #    field values, then reset for next tweet.
                                    
                                    # create tweet instance
                                    create_status = self.create_tweet_instance( current_record_values )
                                    
                                    # reset stuff
                                    current_record_values = {}
                                    empty_line_counter = 0
                                    last_field_name = ""
                                    current_field_name = ""
                                
                                #-- END check to see if first line of a new record. --#
                                
                                print( "Found either non-empty line, or empty line within a tweet.  Process." )
                                
                                # first, parse on first tab in line to look for
                                #    field name.
                                split_tweet_list = current_line.split( "\t", 1 )
                                
                                # got more than one thing?
                                if ( len( split_tweet_list ) > 1 ):
                                
                                    # we do.  Get name and value.
                                    field_name_string = split_tweet_list[ 0 ]
                                    field_value_string = split_tweet_list[ 1 ]
                                    
                                    # is name one of our field names?
                                    is_field_name = field_name_string in self.FIELD_NAME_LIST
                                    if ( is_field_name == True ):
                                    
                                        # so, looks like we've found the next
                                        #    field.  Reset things.
                                        last_field_name = current_field_name
                                        current_field_name = field_name_string
                                        
                                        # store the value for the field.
                                        
                                        # first, see if there is already a value.
                                        if ( current_field_name in current_record_values ):
                                        
                                            # already there - append.
                                            current_record_values[ current_field_name ] = current_record_values[ current_field_name ] + current_line
                                        
                                        else:
                                        
                                            # not already there.  Set.
                                            current_record_values[ current_field_name ] = field_value_string
                                            
                                        #-- END check to see if already a value for the field. --#

                                    else:
                                    
                                        # not a field name.  Are we in a field?
                                        if ( current_field_name != "" ):
                                        
                                            # first, see if there is already a value.
                                            if ( current_field_name in current_record_values ):
                                            
                                                # already there - append.
                                                current_record_values[ current_field_name ] = current_record_values[ current_field_name ] + current_line
                                            
                                            else:
                                            
                                                # not already there.  Set.
                                                current_record_values[ current_field_name ] = field_value_string
                                                
                                            #-- END check to see if already a value for the field. --#
    
                                        else:
                                        
                                            print( self.STATUS_ERROR_PREFIX + "In " + me + "(): current line doesn't have a field name, and no current field name set, so don't know what to do with it. Line " + str( line_counter ) + ": " + current_line )
                                        
                                        #-- END - check to see if there is a current field to add this to. --#
                                    
                                    #-- END - check to see if we have a field name. --#
                                    
                                else: # line that doesn't contain a tab.
                                
                                    # are we in a field?
                                    if ( current_field_name != "" ):
                                    
                                        # add this line to the value for tweet text.
                                        current_record_values[ current_field_name ] = current_record_values[ current_field_name ] + current_line
                                    
                                    else:
                                    
                                        # error - non-empty line, no name-value
                                        #    pair, not in text field.
                                        print( self.STATUS_ERROR_PREFIX + "In " + me + "(): current line doesn't have a tab, and no current field name set, so don't know what to do with it. Line " + str( line_counter ) + ": " + current_line )
                                    
                                    #-- END check to see if we are in the text field. --#
                                    
                                #-- END check to see if split resulted in anything. --#
                                
                            else:
                                
                                # empty. Increment empty line count.
                                empty_line_counter += 1
                                
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