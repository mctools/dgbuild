include_guard()

get_filename_component( EXTRACT_DEPINFO_PYSCRIPT "${CMAKE_CURRENT_LIST_DIR}/extract_flags_helper.py" REALPATH )

function( extract_extdep_flags language find_package_arg_list deptargets_list cmake_args_list resvar_cflags resvar_linkflags )
  set( cmd python3 "${EXTRACT_DEPINFO_PYSCRIPT}"
    --cmakecommand "${CMAKE_COMMAND}" --respectcmakeargs
    -l "${language}"
    -f -o stdout_json )
  string(JOIN "@@" tmp ${find_package_arg_list})
  list( APPEND cmd --findpackage "${tmp}" )
  string(JOIN "@@" tmp ${deptargets_list})
  list( APPEND cmd --deptargets "${tmp}" )
  if ( cmake_args_list )
    list( APPEND cmd -- )
    foreach( tmp ${cmake_args_list} )
      if ( tmp )
        list( APPEND cmd "${tmp}" )
      endif()
    endforeach()
  endif()
  if ( DG_VERBOSE )
    string( JOIN " " tmp ${cmd} )
    message( STATUS "About to execute: ${tmp}" )
  endif()
  execute_process( COMMAND ${cmd} OUTPUT_VARIABLE tmp COMMAND_ERROR_IS_FATAL ANY )
  string(JSON obj_extra GET "${tmp}" "extra")
  string(JSON array_cf GET "${obj_extra}" "compileflags")
  string(JSON array_lf GET "${obj_extra}" "linkflags")
  string(JSON arraylen_cf LENGTH ${array_cf})
  string(JSON arraylen_lf LENGTH ${array_lf})
  set( res_cf "" )
  set( res_lf "" )
  if ( arraylen_cf )
    math(EXPR idxmax "${arraylen_cf}-1")
    foreach( idx RANGE ${idxmax} )
      string( JSON elem GET "${array_cf}" ${idx} )
      list( APPEND res_cf "${elem}" )
    endforeach()
  endif()
  if ( arraylen_lf )
    math(EXPR idxmax "${arraylen_lf}-1")
    foreach( idx RANGE ${idxmax} )
      string( JSON elem GET "${array_lf}" ${idx} )
      list( APPEND res_lf "${elem}" )
    endforeach()
  endif()
  set( ${resvar_cflags} "${res_cf}" PARENT_SCOPE )
  set( ${resvar_linkflags} "${res_lf}" PARENT_SCOPE )
endfunction()
