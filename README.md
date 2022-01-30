# poetry-sample

## 既存プロジェクトへの poetry の導入

```sh
git clone https://github.com/SchwarzKatzeZwei/poetry-sample.git
poetry config virtualenvs.in-project true
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

### Reference

<https://pradyunsg.me/furo/reference/>
