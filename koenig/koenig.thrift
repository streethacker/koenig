namespace py koenig

/**
* Exceptions
*/

enum KoenigErrorCode {
    UNKNOWN_ERROR,
    
    // UserErrors
    ACCESS_DENIED,
    DISK_PATH_NOT_FOUND,
    PARAMETER_TYPE_INVALID,
    
    // SystemErrors
    PROCESS_NOT_FOUND,
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
*/

/**
* CPU
*/

struct TCPUTimes {
    1: required double user,
    2: required double system,
    3: required double idle,

    4: optional double nice,
    5: optional double iowait,
    6: optional double irq,
    7: optional double softirq,
    8: optional double steal,

    9: optional double guest,
    10: optional double guest_nice,
}


struct TCPUTimesPercent {
    1: required double user,
    2: required double system,
    3: required double idle,
    
    4: optional double nice,
    5: optional double iowait,
    6: optional double irq,
    7: optional double softirq,
    8: optional double steal,
    
    9: optional double guest,
    10: optional double guest_nice,     
}


/**
* MEMORY
*/

struct TVirtualMemory {
    1: required i64 total,
    2: required i64 available,
    3: required double percent,
    4: required i64 used,
    5: required i64 free,
    
    6: required i64 active,
    7: required i64 inactive,
    8: required i64 buffers,
    9: required i64 cached,
    10: required i64 wired,
    11: required i64 shared,    
}


struct TSwapMemory {
    1: required i64 total,
    2: required i64 used,
    3: required i64 free,
    4: required double percent,
    5: required i64 sin,
    6: required i64 sout,    
}


/**
* DISK
*/

struct TDiskPartition {
    1: required string device,
    2: required string mountpoint,
    3: required string fstype,
    4: required string opts,    
}


struct TDiskUsage {
    1: required i64 total,
    2: required i64 used,
    3: required i64 free,
    4: required double percent,    
}


struct TDiskIOCounters {
    1: required i64 read_count,
    2: required i64 write_count,
    3: required i64 read_bytes,
    4: required i64 write_bytes,
    5: required i64 read_time,
    6: required i64 write_time,    
}


/**
* NETWORK
*/

struct TNetworkAddress {
    1: optional string ip,
    2: optional i32 port,
}


struct TNetworkIOCounters {
    1: required i64 bytes_sent,
    2: required i64 bytes_recv,
    3: required i64 packets_sent,
    4: required i64 packets_recv,

    5: required i16 errin,
    6: required i16 errout,
    7: required i16 dropin,
    8: required i16 dropout,
}


struct TNetworkConnections {
    1: required i16 fd,
    2: required i16 family,
    4: required i16 type,

    5: required TNetworkAddress laddr,
    6: required TNetworkAddress raddr,

    7: required string status,
    8: required i32 pid,   
}


/**
* USERS
*/

struct TUser {
    1: required string name,
    2: required string terminal,
    3: required string host,
    4: required double started,    
}


/**
* PROCESSES
*/

struct TProcessUID {
    1: required i32 real,
    2: required i32 effective,
    3: required i32 saved,    
}

struct TProcessGID {
    1: required i32 real,
    2: required i32 effective,
    3: required i32 saved,    
}

struct TProcess {
    1: required i32 pid,
    2: required i32 ppid,
    3: required string name,
    4: required string username,
    5: required double create_time,
    6: required double cpu_percent,
    7: required double memory_percent,
    8: required string cwd,
    9: required string status,
    10: required string exe,
    11: required TProcessUID uids,
    12: required TProcessGID gids,    
}


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

    /**
    * query cpu info
    */

    TCPUTimes query_cpu_times()
        throws (
            1: KoenigUserException user_exception,
            2: KoenigSystemException system_exception,
            3: KoenigUnknownException unknown_exception
        )

    list<TCPUTimes> query_cpu_times_percpu()
        throws (
            1: KoenigUserException user_exception,
            2: KoenigSystemException system_exception,
            3: KoenigUnknownException unknown_exception
        )

    double query_cpu_percent(1: i16 interval)
        throws (
            1: KoenigUserException user_exception,
            2: KoenigSystemException system_exception,
            3: KoenigUnknownException unknown_exception
        )

    list<double> query_cpu_percent_percpu(1: i16 interval)
        throws (
            1: KoenigUserException user_exception,
            2: KoenigSystemException system_exception,
            3: KoenigUnknownException unknown_exception
        )

    TCPUTimesPercent query_cpu_times_percent(1: i16 interval)
        throws (
            1: KoenigUserException user_exception,
            2: KoenigSystemException system_exception,
            3: KoenigUnknownException unknown_exception
        )

    list<TCPUTimesPercent> query_cpu_times_percent_percpu(1: i16 interval)
        throws (
            1: KoenigUserException user_exception,
            2: KoenigSystemException system_exception,
            3: KoenigUnknownException unknown_exception
        )

    /**
    * query memory info
    */

    TVirtualMemory query_virtual_memory()
        throws (
            1: KoenigUserException user_exception,
            2: KoenigSystemException system_exception,
            3: KoenigUnknownException unknown_exception
        )

    TSwapMemory query_swap_memory()
        throws (
            1: KoenigUserException user_exception,
            2: KoenigSystemException system_exception,
            3: KoenigUnknownException unknown_exception
        )

    /**
    * query disk info
    */

    list<TDiskPartition> query_disk_partitions()
        throws (
            1: KoenigUserException user_exception,
            2: KoenigSystemException system_exception,
            3: KoenigUnknownException unknown_exception
        )

    TDiskIOCounters query_disk_io_counters()
        throws (
            1: KoenigUserException user_exception,
            2: KoenigSystemException system_exception,
            3: KoenigUnknownException unknown_exception
        )

    map<string, TDiskIOCounters> query_disk_io_counters_perdisk()
        throws (
            1: KoenigUserException user_exception,
            2: KoenigSystemException system_exception,
            3: KoenigUnknownException unknown_exception
        )

    TDiskUsage query_disk_usage(1: string path)
        throws (
            1: KoenigUserException user_exception,
            2: KoenigSystemException system_exception,
            3: KoenigUnknownException unknown_exception
        )

    /**
    * query network io info
    */

    TNetworkIOCounters query_net_io_counters()
        throws (
            1: KoenigUserException user_exception,
            2: KoenigSystemException system_exception,
            3: KoenigUnknownException unknown_exception
        )

    map<string, TNetworkIOCounters> query_net_io_counters_pernic()
        throws (
            1: KoenigUserException user_exception,
            2: KoenigSystemException system_exception,
            3: KoenigUnknownException unknown_exception
        )

    list<TNetworkConnections> query_net_connections()
        throws (
            1: KoenigUserException user_exception,
            2: KoenigSystemException system_exception,
            3: KoenigUnknownException unknown_exception
        )

    /**
    * query login info
    */

    list<TUser> query_login_users()
        throws (
            1: KoenigUserException user_exception,
            2: KoenigSystemException system_exception,
            3: KoenigUnknownException unknown_exception
        )

    string query_boot_time()
        throws (
            1: KoenigUserException user_exception,
            2: KoenigSystemException system_exception,
            3: KoenigUnknownException unknown_exception
        )

    /**
    * query process info
    */

    list<i32> query_pids()
        throws (
            1: KoenigUserException user_exception,
            2: KoenigSystemException system_exception,
            3: KoenigUnknownException unknown_exception
        )

    TProcess query_process_by_pid(1: i32 pid)
        throws (
            1: KoenigUserException user_exception,
            2: KoenigSystemException system_exception,
            3: KoenigUnknownException unknown_exception
        )

    map<i32, TProcess> query_processes_by_pids(1: list<i32> pids)
        throws (
            1: KoenigUserException user_exception,
            2: KoenigSystemException system_exception,
            3: KoenigUnknownException unknown_exception
        )
}
