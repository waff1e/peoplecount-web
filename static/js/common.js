
!function(){
    window.common = {};

    common.use_data = function(data){
        var now_data = data;

        if(typeof now_data === 'string'){
            now_data = JSON.parse(now_data);
        } else {
            now_data = now_data;
        }

        return now_data;
    };
    
    common.check_datas = function(params){
        var option = $.extend({
            data: [null],
            type: [null],
            return_data : {
                result : false,
                msg : '',
                focus : null
            }
            }, params)

        for(var i = 0; i<option.data.length; i++){
            if(option.data[i].val() == ''){
                option.return_data.msg = error_data[option.type[i]].no_data;
                option.data[i].focus();
                return option.return_data;
            }
        }
        option.return_data.result = true;
        return option.return_data;

    }

    error_data = {
        'id' : {
            'no_data': "아이디를 입력해주세요.",
        },
        'pw' : {
            'no_data': "비밀번호를 입력해주세요.",
        }
    }

    common.ajax = function(params){
        var option = $.extend({
            url: null,
            type: 'GET',
            dataType : 'json',
            data: null,
            callback : null
            }, params)

        $.ajax({
            url : option.url,
            type : option.type,
            dataType : option.dataType,
            data: option.data,
            success : function(data){
                var datas = common.use_data(data);
                if(datas.result == 'success'){

                }else{
                    alert(datas.msg);
                }
                if(typeof(option.callback) == "function"){
                    option.callback(datas);
                }
            },
            error : function(){
                alert('통신실패!!');
            },

        });

    }

}();