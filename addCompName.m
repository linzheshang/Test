function [ output_data ] = addCompName( input_data )
%在表格第二列根据股票代码添加股票中文简称
sqlname='select distinct s_info_windcode,s_info_name from AShareDescription order by s_info_windcode';
conn=DBlinkWind();
compname=DBFetch(conn ,sqlname);    %获取数据
[~,seq_name]=ismember(input_data(:,1),compname(:,1));
if isnan(seq_name)
    disp('所有股票代码都无法添加简称');
elseif isempty(find(seq_name==0))==0%存在部分无法添加简称的股票
    seq=find(seq_name==0);
    Notice=[num2str(seq),' 列无法添加股票简称'];
    disp(Notice);
    output_data=[num2cell(zeros(size(input_data,1),1)),input_data];
    for i=1:length(seq_name)
        a=seq_name(i,1);
        if a~=0
            output_data{a,1}=compname{a,2};%在第一列加入股票名称
        end
    end
else
    output_data=[compname(seq_name,2),input_data];
end

