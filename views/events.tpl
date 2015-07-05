% rebase('base.tpl', title='勉強会の一覧')
    <h1>勉強会の一覧</h1>
    % for event in events:
        <p><a href="{{event['event_url']}}">{{event['title']}}</a></p>
    %
