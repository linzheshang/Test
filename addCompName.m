function [ output_data ] = addCompName( input_data )
%�ڱ��ڶ��и��ݹ�Ʊ������ӹ�Ʊ���ļ��
sqlname='select distinct s_info_windcode,s_info_name from AShareDescription order by s_info_windcode';
conn=DBlinkWind();
compname=DBFetch(conn ,sqlname);    %��ȡ����
[~,seq_name]=ismember(input_data(:,1),compname(:,1));
if isnan(seq_name)
    disp('���й�Ʊ���붼�޷���Ӽ��');
elseif isempty(find(seq_name==0))==0%���ڲ����޷���Ӽ�ƵĹ�Ʊ
    seq=find(seq_name==0);
    Notice=[num2str(seq),' ���޷���ӹ�Ʊ���'];
    disp(Notice);
    output_data=[num2cell(zeros(size(input_data,1),1)),input_data];
    for i=1:length(seq_name)
        a=seq_name(i,1);
        if a~=0
            output_data{a,1}=compname{a,2};%�ڵ�һ�м����Ʊ����
        end
    end
else
    output_data=[compname(seq_name,2),input_data];
end

