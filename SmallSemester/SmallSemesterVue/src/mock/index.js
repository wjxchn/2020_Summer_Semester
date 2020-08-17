import Mock from 'mockjs'

var {TeamList} = Mock.mock({
    'TeamList|4-8': [
        {
            "id":"@increment()",
            "name":'@ctitle(4,7)',
            "personList|50-100":{
                "name":'@cname()',
            },
            "owner":'@cname()',
            "time":'@date(yyyy/MM/dd hh:mm:ss)',
            "introduction":'@cparagraph(5,50)'
        }
    ]
})
var {PersonalDocList} = Mock.mock({
    'PersonalDocList|4-8': [
        {
            "doc_id":"@increment",
            "id":"@increment()",
            "docname":'@ctitle(4,7)',
            "creator":'@cname()',
            "belong":'@cname()',
            "createtime":'@date(yyyy/MM/dd hh:mm:ss)',
        }
    ]
})
var {TeamDocList} = Mock.mock({
    'TeamDocList|4-8': [
        {
            "docid":"@increment",
            "docname":'@ctitle(4,7)',
            "creator":'@cname()',
            "belong":'@cname()',
            "creation_time":'@date(yyyy/MM/dd hh:mm:ss)',
        }
    ]
})
var {PersonList} = Mock.mock({
    'PersonList|4-8': [
        {
            "username":"@cname()"
        }
    ]
})
Mock.mock('http://localhost:8000/api/returnusername/','post',(options)=>{
    return{
        code:200,
        message:'获取用户名列表成功',
        list:PersonList,
        total:PersonList.length
    }
})
Mock.mock('http://localhost:8000/api/show_group_doclist/','post',(options)=>{
    return{
        code:200,
        message:'获取团队文档列表成功',
        list:TeamDocList,
        total:TeamDocList.length
    }
})
var {MessageList} = Mock.mock({
    'MessageList|8-10': [
        {
            "id":"@increment()",
            "MessageTitle":'@ctitle(7,15)',
            "date":'@date(yyyy/MM/dd hh:mm:ss)',
            "MessageContent":'@cparagraph(5,50)'
        }
    ]
})
Mock.mock('http://localhost:8000/api/showpersonaldoclist/','post',(options)=>{
    return{
        code:200,
        message:'获取个人文档列表成功',
        list:PersonalDocList,
        total:PersonalDocList.length
    }
})
Mock.mock('/api/post/messagelist','post',(options)=>{
    return{
        status:200,
        message:'获取消息列表成功',
        MessageList:MessageList,
        total: MessageList.length
    }
})
Mock.mock('/api/post/teamlist','post',(options)=>{
    return{
        status:200,
        message:'获取团队列表成功',
        sideData:TeamList,
        total: TeamList.length
    }
})
Mock.mock('api/post/add/Team','post',(options)=>{
    const body = JSON.parse(options.body)
    TeamList.push(Mock.mock({
        "id":"@increment()",
            "name":body.name,
            "personList|50-100":{
                "name":'@cname()',
            },
            "owner":body.owner,
            "time":body.time,
            "introduction":body.introduction
    }))
    return{
        status:200,
        message:'添加成功',
        sideData:TeamList,
        total: TeamList.length
    }
})
Mock.mock('http://localhost:8000/api/addgroupdoc/','post',(options)=>{
    const body = JSON.parse(options.body)
    TeamDocList.push(Mock.mock({
        "docid":"@increment",
        "docname":body.list.docname,
        "creator":body.username,
        "creation_time":body.list.createtime,
    }))
    return{
        status:200,
        message:'添加成功',
        sideData:TeamList,
        total: TeamList.length
    }
})