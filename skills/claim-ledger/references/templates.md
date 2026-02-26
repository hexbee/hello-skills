# Claim Ledger Templates

## Ledger 表（最小版）

```text
| ID  | Claim | Type | Conf | Evidence (E#) | Source Grade | Counter | Boundary | Publish |
|-----|-------|------|------|---------------|--------------|---------|----------|---------|
| C01 | ...   | ...  | ...  | E01,E02       | A,B          | ...     | ...      | ...     |
| C02 | ...   | ...  | ...  | E03,E04       | S,A          | ...     | ...      | ...     |
| C03 | ...   | ...  | ...  | E05,E06       | A,B          | ...     | ...      | ...     |
```

## Evidence Card（每条 E# 一段）

```text
E01
- Source: 标题 + 作者/机构 + 日期
- Link: URL 或文档定位
- Quote/Data: 可复核原话或数字
- Supports: 支持 C0X 的哪一段
- Reliability: S/A/B/⚠️，以及评级理由
- Freshness: 是/否（是否过时）
```

## Gate Check（正文前检查）

```text
Gate Check
- [ ] 每条 Claim >= 2 条证据
- [ ] 每条 Claim >= 1 条反证/反例
- [ ] 每条 Claim 有成立条件与失效条件
- [ ] 预测/建议型 Claim 有失败条件
- [ ] 证据不足的 Claim 已降级为低置信度并降调语气
```

## 线程映射模板（12 条）

```text
Claim 1:
1) Claim
2) Evidence
3) Boundary
4) Action

Claim 2:
5) Claim
6) Evidence
7) Boundary
8) Action

Claim 3:
9) Claim
10) Evidence
11) Boundary
12) Action
```

