```eval_rst
:orphan:
```

# 画面設計書 - A 画面

スフィンクスで書く最初のドキュメントです。

## 章立て

第一章

## markdown table

| TH  | TH  |
| --- | --- |
| TD  | TD  |
| TD  | TD  |

## code 挿入

```py
import sphinx_fontawesome
sys.path.insert(0, os.path.abspath("../../poetry_dev/"))
```

## 数式

```math
E = m c^2
```

## 画像挿入

![img](https://notepm-projectmode-stg.s3-ap-northeast-1.amazonaws.com/help/table/table-editor500.gif)

![img2](img.drawio.svg)

```eval_rst
.. note::
    This is what the most basic admonitions look like.

.. admonition:: Another Custom Title
    :class: attention

    内容
```

## ブロック図

```eval_rst
.. blockdiag::

    blockdiag admin {
      top_page -> config -> config_edit -> config_confirm -> top_page;
    }
```

## シーケンス図

```eval_rst
.. seqdiag::

    seqdiag admin {
      A -> B -> C -> D -> E -> F -> G;
    }
```

## アクティビティ図

```eval_rst
.. actdiag::

    actdiag admin {
      A -> B -> C;
    }
```

## ネットワーク図

```eval_rst
.. nwdiag::
   :desctable:

   nwdiag {
      network {
        A [address = 192.168.0.1, description = "web server01"];
        B [address = 192.168.0.2, description = "web server02"];
      }
      network {
        A [address = 172.0.0.1];
        C [address = 172.0.0.2, description = "database server"];
      }
   }
```

## ラック図

```eval_rst
.. rackdiag::
    :desctable:

    rackdiag {
        rack {
            10U

            description = "Rack No. 001 Production";

            1: Switching HUB [0.5A,description="Cisco"]
            2: Web Server 01 [0.5A,description="HP"]
            3: Web Server 02 [0.5A,description="HP"]
            4: Application Server 01 [0.5A,description="HP"]
            5: Application Server 02 [0.5A,description="HP"]
            6: DB Server 01 [2U,1A,description="HP"]
            8: DB Server 02 [2U,1A,description="HP"]
            10: N/A
        }
        rack {
            10U

            description = "Rack No. 002 Test";

            1: Switching HUB [0.5A,description="Cisco"]
            2: Web Server [0.5A,description="HP"]
            3: Application Server [0.5A,description="HP"]
            4: DB Server [2U,1A,description="HP"]
            6: N/A [5U]
        }
    }
```

## パケットヘッダ図

```eval_rst
.. packetdiag::
    :desctable:

    {
        colwidth = 32
        node_height = 72

        0-15: Source Port
        16-31: Destination Port
        32-63: Sequence Number
        64-95: Acknowledgment Number
        96-99: Data Offset
        100-105: Reserved
        106: URG [rotate = 270]
        107: ACK [rotate = 270]
        108: PSH [rotate = 270]
        109: RST [rotate = 270]
        110: SYN [rotate = 270]
        111: FIN [rotate = 270]
        112-127: Window
        128-143: Checksum
        144-159: Urgent Pointer
        160-191: (Options and Padding)
        192-223: data [colheight = 3]
    }
```
