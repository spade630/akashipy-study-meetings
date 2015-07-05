% rebase('base.tpl', title='勉強会の一覧')
    <h1>勉強会の一覧</h1>
    <form action="/events" method="GET">
        <input type="text" name="keyword">
        <button type="button">検索</button>
    </form>
    % for event in events:
        <p><a href="{{event['event_url']}}">{{event['title']}}</a></p>
    %
