# poetry-sample

## poetry インストール

1. pyenvと連携する場合

   [Poetry documentation](https://cocoatomo.github.io/poetry-ja/)

   プロジェクトディレクトリにて`pyenv local 3.x.x`と実行して使う。

2. anacondaと連携する場合

   ```sh
   conda install poetry
   ```

   `conda activate xxx`と実行して使う

## 環境準備

```sh
git clone https://github.com/SchwarzKatzeZwei/poetry-sample.git
poetry config virtualenvs.in-project true  # 仮想環境をプロジェクトディレクトリ内で構築
poetry init
poetry install
```

## VSCode との Lint 連携

1. インタープリター選択

   `.venv/bin/python`

2. pflake8 の設定

   ワークスペースの setting.json に以下を設定

   `"python.linting.flake8Path": ".venv/bin/pflake8"`

## 設計書作成

### python -> rst 生成

```sh
poetry shell
sphinx-apidoc -f -e -o ./docs/source ./src
```

### HTML 生成

```sh
poetry shell
make html # build
# or
make livehtml # auto build
```

> Furo Theme Reference  
> <https://pradyunsg.me/furo/reference/>
