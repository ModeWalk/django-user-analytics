/*
 * Django User Analytics support files
 *
 * https://github.com/RBURHUM/django-user-analytics
 *
 * Copyright 2012, Ragi Burhum
 * Dual licensed under the MIT or GPL Version 2 licenses.
 * http://www.opensource.org/licenses/mit-license.php
 * http://www.opensource.org/licenses/GPL-2.0
 */

$(function(){
    // check if cookie verification is set
    // trigger a get to set csrf token

    if ($.cookie('yb_verify') !== null){
        $.post('ua-yb/verify', function(data) {
        });
    }
});
