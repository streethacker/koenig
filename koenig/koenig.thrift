namespace py koenig

/**
* Exceptions
*/

enum KoenigErrorCode {
    UNKNOWN_ERROR,
    
    // UserErrors
    ACCESS_DENIED,
    
    // SystemErrors
    PLATFORM_NOT_SUPPORT,    
}

exception KoenigUserException {
    1: required KoenigErrorCode error_code,
    2: required string error_name,
    3: required string message,    
}

exception KoenigSystemException {
    1: required KoenigErrorCode error_code,
    2: required string error_name,
    3: required string message,    
}

exception KoenigUnknownException {
    1: required KoenigErrorCode error_code,
    2: required string error_name,
    3: required string message,    
}


/**
* Types & Structs

/**


* Services
**/

service KoenigService {
    
    bool ping()
        throws (
            1: KoenigUserException user_exception,
            2: KoenigSystemException system_exception,
            3: KoenigUnknownException unknown_exception
        )

}
