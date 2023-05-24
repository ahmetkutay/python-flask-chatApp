HTTP_CONTINUE = 100
HTTP_SWITCHING_PROTOCOLS = 101
HTTP_PROCESSING = 102
HTTP_EARLY_HINTS = 103
HTTP_OK = 200
HTTP_CREATED = 201
HTTP_ACCEPTED = 202
HTTP_NON_AUTHORITATIVE_INFORMATION = 203
HTTP_NO_CONTENT = 204
HTTP_RESET_CONTENT = 205
HTTP_PARTIAL_CONTENT = 206
HTTP_MULTI_STATUS = 207
HTTP_ALREADY_REPORTED = 208
HTTP_IM_USED = 226
HTTP_MULTIPLE_CHOICES = 300
HTTP_MOVED_PERMANENTLY = 301
HTTP_FOUND = 302
HTTP_SEE_OTHER = 303
HTTP_NOT_MODIFIED = 304
HTTP_USE_PROXY = 305
HTTP_TEMPORARY_REDIRECT = 307
HTTP_PERMANENT_REDIRECT = 308
HTTP_BAD_REQUEST = 400
HTTP_UNAUTHORIZED = 401
HTTP_PAYMENT_REQUIRED = 402
HTTP_FORBIDDEN = 403
HTTP_NOT_FOUND = 404
HTTP_METHOD_NOT_ALLOWED = 405
HTTP_NOT_ACCEPTABLE = 406
HTTP_PROXY_AUTHENTICATION_REQUIRED = 407
HTTP_REQUEST_TIMEOUT = 408
HTTP_CONFLICT = 409
HTTP_GONE = 410
HTTP_LENGTH_REQUIRED = 411
HTTP_PRECONDITION_FAILED = 412
HTTP_PAYLOAD_TOO_LARGE = 413
HTTP_URI_TOO_LONG = 414
HTTP_UNSUPPORTED_MEDIA_TYPE = 415
HTTP_RANGE_NOT_SATISFIABLE = 416
HTTP_EXPECTATION_FAILED = 417
HTTP_IM_A_TEAPOT = 418
HTTP_MISDIRECTED_REQUEST = 421
HTTP_UNPROCESSABLE_ENTITY = 422
HTTP_LOCKED = 423
HTTP_FAILED_DEPENDENCY = 424
HTTP_TOO_EARLY = 425
HTTP_UPGRADE_REQUIRED = 426
HTTP_PRECONDITION_REQUIRED = 428
HTTP_TOO_MANY_REQUESTS = 429
HTTP_REQUEST_HEADER_FIELDS_TOO_LARGE = 431
HTTP_UNAVAILABLE_FOR_LEGAL_REASONS = 451
HTTP_INTERNAL_SERVER_ERROR = 500
HTTP_NOT_IMPLEMENTED = 501
HTTP_BAD_GATEWAY = 502
HTTP_SERVICE_UNAVAILABLE = 503
HTTP_GATEWAY_TIMEOUT = 504
HTTP_HTTP_VERSION_NOT_SUPPORTED = 505
HTTP_VARIANT_ALSO_NEGOTIATES = 506
HTTP_INSUFFICIENT_STORAGE = 507
HTTP_LOOP_DETECTED = 508
HTTP_NOT_EXTENDED = 510
HTTP_NETWORK_AUTHENTICATION_REQUIRED = 511

HTTP_STATUS_CODES = {
    'HTTP_CONTINUE': HTTP_CONTINUE,
    'HTTP_SWITCHING_PROTOCOLS': HTTP_SWITCHING_PROTOCOLS,
    'HTTP_PROCESSING': HTTP_PROCESSING,
    'HTTP_EARLY_HINTS': HTTP_EARLY_HINTS,
    'HTTP_OK': HTTP_OK,
    'HTTP_CREATED': HTTP_CREATED,
    'HTTP_ACCEPTED': HTTP_ACCEPTED,
    'HTTP_NON_AUTHORITATIVE_INFORMATION': HTTP_NON_AUTHORITATIVE_INFORMATION,
    'HTTP_NO_CONTENT': HTTP_NO_CONTENT,
    'HTTP_RESET_CONTENT': HTTP_RESET_CONTENT,
    'HTTP_PARTIAL_CONTENT': HTTP_PARTIAL_CONTENT,
    'HTTP_MULTI_STATUS': HTTP_MULTI_STATUS,
    'HTTP_ALREADY_REPORTED': HTTP_ALREADY_REPORTED,
    'HTTP_IM_USED': HTTP_IM_USED,
    'HTTP_MULTIPLE_CHOICES': HTTP_MULTIPLE_CHOICES,
    'HTTP_MOVED_PERMANENTLY': HTTP_MOVED_PERMANENTLY,
    'HTTP_FOUND': HTTP_FOUND,
    'HTTP_SEE_OTHER': HTTP_SEE_OTHER,
    'HTTP_NOT_MODIFIED': HTTP_NOT_MODIFIED,
    'HTTP_USE_PROXY': HTTP_USE_PROXY,
    'HTTP_TEMPORARY_REDIRECT': HTTP_TEMPORARY_REDIRECT,
    'HTTP_PERMANENT_REDIRECT': HTTP_PERMANENT_REDIRECT,
    'HTTP_BAD_REQUEST': HTTP_BAD_REQUEST,
    'HTTP_UNAUTHORIZED': HTTP_UNAUTHORIZED,
    'HTTP_PAYMENT_REQUIRED': HTTP_PAYMENT_REQUIRED,
    'HTTP_FORBIDDEN': HTTP_FORBIDDEN,
    'HTTP_NOT_FOUND': HTTP_NOT_FOUND,
    'HTTP_METHOD_NOT_ALLOWED': HTTP_METHOD_NOT_ALLOWED,
    'HTTP_NOT_ACCEPTABLE': HTTP_NOT_ACCEPTABLE,
    'HTTP_PROXY_AUTHENTICATION_REQUIRED': HTTP_PROXY_AUTHENTICATION_REQUIRED,
    'HTTP_REQUEST_TIMEOUT': HTTP_REQUEST_TIMEOUT,
    'HTTP_CONFLICT': HTTP_CONFLICT,
    'HTTP_GONE': HTTP_GONE,
    'HTTP_LENGTH_REQUIRED': HTTP_LENGTH_REQUIRED,
    'HTTP_PRECONDITION_FAILED': HTTP_PRECONDITION_FAILED,
    'HTTP_PAYLOAD_TOO_LARGE': HTTP_PAYLOAD_TOO_LARGE,
    'HTTP_URI_TOO_LONG': HTTP_URI_TOO_LONG,
    'HTTP_UNSUPPORTED_MEDIA_TYPE': HTTP_UNSUPPORTED_MEDIA_TYPE,
    'HTTP_RANGE_NOT_SATISFIABLE': HTTP_RANGE_NOT_SATISFIABLE,
    'HTTP_EXPECTATION_FAILED': HTTP_EXPECTATION_FAILED,
    'HTTP_IM_A_TEAPOT': HTTP_IM_A_TEAPOT,
    'HTTP_MISDIRECTED_REQUEST': HTTP_MISDIRECTED_REQUEST,
    'HTTP_UNPROCESSABLE_ENTITY': HTTP_UNPROCESSABLE_ENTITY,
    'HTTP_LOCKED': HTTP_LOCKED,
    'HTTP_FAILED_DEPENDENCY': HTTP_FAILED_DEPENDENCY,
    'HTTP_TOO_EARLY': HTTP_TOO_EARLY,
    'HTTP_UPGRADE_REQUIRED': HTTP_UPGRADE_REQUIRED,
    'HTTP_PRECONDITION_REQUIRED': HTTP_PRECONDITION_REQUIRED,
    'HTTP_TOO_MANY_REQUESTS': HTTP_TOO_MANY_REQUESTS,
    'HTTP_REQUEST_HEADER_FIELDS_TOO_LARGE': HTTP_REQUEST_HEADER_FIELDS_TOO_LARGE,
    'HTTP_UNAVAILABLE_FOR_LEGAL_REASONS': HTTP_UNAVAILABLE_FOR_LEGAL_REASONS,
    'HTTP_INTERNAL_SERVER_ERROR': HTTP_INTERNAL_SERVER_ERROR,
    'HTTP_NOT_IMPLEMENTED': HTTP_NOT_IMPLEMENTED,
    'HTTP_BAD_GATEWAY': HTTP_BAD_GATEWAY,
    'HTTP_SERVICE_UNAVAILABLE': HTTP_SERVICE_UNAVAILABLE,
    'HTTP_GATEWAY_TIMEOUT': HTTP_GATEWAY_TIMEOUT,
    'HTTP_HTTP_VERSION_NOT_SUPPORTED': HTTP_HTTP_VERSION_NOT_SUPPORTED,
    'HTTP_VARIANT_ALSO_NEGOTIATES': HTTP_VARIANT_ALSO_NEGOTIATES,
    'HTTP_INSUFFICIENT_STORAGE': HTTP_INSUFFICIENT_STORAGE,
    'HTTP_LOOP_DETECTED': HTTP_LOOP_DETECTED,
    'HTTP_NOT_EXTENDED': HTTP_NOT_EXTENDED,
    'HTTP_NETWORK_AUTHENTICATION_REQUIRED': HTTP_NETWORK_AUTHENTICATION_REQUIRED,
}