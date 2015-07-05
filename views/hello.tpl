% rebase('base.tpl', title='Bottleの練習')

<h1>Hello {{name}}!</h1>
<p>//はろーわーるどを表示</p>

<form action="/events" method="GET">
    <input type="text" name="keyword">
    <button type="button">検索</button>
</form>