'use strict';

$.notify = function (message, title, time) {
    var $the = $($('#the-notification').html());
    if (undefined !== title) {
        $the.find('.toast-title').text(title);
    }
    if (undefined === time) {
        $the.find('.toast-time').hide()
    } else {
        $the.find('.toast-time').text(time).show();
    }
    if (undefined !== message) {
        $the.find('.toast-body').html(message);
    }
    var $display = $('#the-toast-wrapper');
    $the.prependTo($display);
    $the.toast({
        // autohide: false,
        delay: 5000
    }).toast('show');
}

/**
 * Sort and save jQuery plugin for lists and tables to save position on the server.
 * @example
 * <ul data-action="/pos">
 *   <li data-row="1">
 *     First
 *   </li>
 *   <li data-row="2">
 *     Second
 *     <input type="checkbox" name="is_enabled" checked>
 *   </li>
 * </ul>
 * @param object options The plugin options.
 * @param function The callback function.
 * @example
 *   object {
 *     sort: false | true,
 *     switch: false | true | 'selector'
 *   },
 *   function (method, element, response, request)
 */
$.fn.manipulate = function () {
    var callback = null;
    var options = {
        sort: true,
        switch: false,
        delete: true
    };
    for (var i = 0; i < arguments.length; i++) {
        var arg = arguments[i];
        if ('function' === typeof arg) {
            callback = arg;
        } else if ('object' === typeof arg) {
            options = arg;
        }
    }
    return this.each(function () {
        var o = $.extend({}, options);
        var $this = $(this);
        if (!o.action) {
            $this.parents('[data-action]:first').each(function() {
                o.action = $(this).data('action');
            });
        }
        if (true === o.sort) {
            $this.sortable({
                helper: function(e, ui) {  
                    ui.children().each(function() {  
                        $(this).width($(this).width());  
                    });  
                    return ui;  
                },
                stop: function() {
                    var arr = [], $this = $(this);
                    $this.find('[data-row]').each(function(){
                        arr.push($(this).data('row'));
                    });
                    $this.addClass('ui-loading');
                    var data = {
                        ajax: true,
                        pos: arr
                    };
                    $.post(o.action + '/pos', data, function(response) {
                        $this.removeClass('ui-loading');
                        if ('function' === typeof callback) {
                            callback.call('sort', $this.get(0), response, data);
                        }
                    });
                }
            });            
        }
        if (o.switch) {
            var name = true === o.switch ? 'input[name="is_enabled"]' : o.switch;
            $this.delegate(o.switch, 'change', function() {
                $this.addClass('ui-loading');
                var $input = $(this);
                var data = {
                    ajax: true,
                    id: $input.parents('[data-row]:first').data('row'),
                    name: $input.attr('name'),
                    value: $input.is(':checked') ? 1 : 0
                };
                $.post(o.action + '/update', data, function (response) {
                    $this.removeClass('ui-loading');
                    if ('function' === typeof callback) {
                        callback.call('switch', $input.get(0), response, data);
                    }
                });
            });
        }
        if (o.delete) {
            $this.undelegate('[delete-trigger]', 'click').delegate('[delete-trigger]', 'click', function (event) {
                event.preventDefault();
                var $a = $(this), text = $a.attr('delete-trigger');
                if ('true' === text.toLowerCase() || !text ) {
                    text = 'Are you sure to delete?';
                }
                var $modal = $('#the-confirmation-dialog');
                $modal.find('.modal-body > p').text(text);

                $modal.unbind('shown.bs.modal').on('shown.bs.modal', function () {
                    $modal.find('[type="submit"]:first').focus();
                });

                $modal.undelegate('[type="submit"]', 'click').delegate('[type="submit"]', 'click', function (event) {
                    event.preventDefault();
                    var $row = $a.parents('[data-row]:first');
                    var id = $row.data('row');
                    $this.addClass('ui-loading');
                    $.ajax({
                        url: o.action + '/delete/' + id,
                        type: 'DELETE',
                        success: function (response) {
                            $this.removeClass('ui-loading');
                            $modal.unbind('hidden.bs.modal').on('hidden.bs.modal', function () {
                                $.notify(response.message.body, response.message.title);
                            });
                            $modal.modal('hide');
                            if ('function' === typeof callback) {
                                callback.call('delete', $a.get(0), response, {id: id});
                            } else {
                                $row.remove();
                            }
                        },
                        fail: function (response) {
                            $modal.modal('hide');
                            $this.removeClass('ui-loading');
                            console.log('Failed: ' + response);
                        }
                    })
                });

                $modal.modal('show');
            });
        }
    });
}
$.fn.sortAndSave = function () {
    var callback = null;
    var options = {
        action: null
    };
    for (var i = 0; i < arguments.length; i++) {
        var arg = arguments[i];
        if ('function' === typeof arg) {
            callback = arg;
        } else if ('object' === typeof arg) {
            options = arg;
        }
    }
    return this.each(function() {
        var o = $.extend({}, options);
        if (!o.action) {
            $(this).parents('[data-action]:first').each(function() {
                o.action = $(this).data('action');
            });
        }
        $(this).sortable({
            helper: function(e, ui) {  
                ui.children().each(function() {  
                    $(this).width($(this).width());  
                });  
                return ui;  
            },
            stop: function() {
                var arr = [], $this = $(this);
                $this.find('[data-row]').each(function(){
                    arr.push($(this).data('row'));
                });
                $this.addClass('ui-loading');
                var data = {
                    ajax: true,
                    pos: arr
                };
                $.post(o.action, data, function(response) {
                    $this.removeClass('ui-loading');
                    if ('function' === typeof callback) {
                        callback.call($this.get(0), response, data);
                    }
                });
            }
        });
    });
};

$.fn.switchAndSave = function (selector) {
    return this.each(function () {
        $(this).delegate(selector, 'change', function (event) {

        });
    });
};

$(function() {
    $('.lazy').Lazy({
        scrollDirection: 'vertical',
        effect: 'fadeIn',
        visibleOnly: true,
        onError: function(element) {
            console.log('error loading ' + element.data('src'));
        }
    });    
});