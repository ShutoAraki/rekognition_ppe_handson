# Step 4 & 5

4. POSTリクエストを受け取れるように`template.yaml`とLambdaを書き換える

HTMLファイルからテキストデータをPOSTしたときに、それを`Hello, xxx!`と表示できることをまずは目指しましょう。

`template.yaml`のどこをどう変えたらPOSTリクエストが通るか考えて試してみましょう！

(Hint 1: まずは「AWS SAM template docs」で検索）

5. HTML/JavaScriptからPOSTリクエストを送って挙動を確認する

これは`object_detect.html`のAPI URLを置き換えるだけで大丈夫です。
