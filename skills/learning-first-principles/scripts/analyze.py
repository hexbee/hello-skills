#!/usr/bin/env python3
"""
学习第一性原理分析器
分析学习行为是否符合第一性原理
"""

import json
import sys
from typing import Dict, List, Tuple

# 原理链
PRINCIPLE_CHAIN = [
    ("学习观", "自学", "补课"),
    ("方法论", "归纳总结", "耗时间"),
    ("加工", "自我输出", "机械抄录"),
    ("输出", "表达重构", "简单重复"),
    ("表达", "逻辑", "形式"),
    ("理解", "实践", "止于理论")
]

# 关键词模式匹配
PATTERNS = {
    "自学驱动性": {
        "positive": ["自己学", "自主", "好奇心", "想学", "目标是", "为了"],
        "negative": ["培训班", "老师教", "被逼", "不得不", "课表", "别人让"]
    },
    "归纳总结性": {
        "positive": ["总结", "提炼", "规律", "框架", "核心", "本质"],
        "negative": ["刷题", "重复", "背", "记", "耗时间", "没思考"]
    },
    "自我输出性": {
        "positive": ["讲出来", "写出来", "输出", "分享", "教别人", "自己的话"],
        "negative": ["抄笔记", "复制", "摘抄", "记录"]
    },
    "表达重构性": {
        "positive": ["重新组织", "换个角度", "画图", "类比", "重组"],
        "negative": ["原文", "原话", "照搬", "一样"]
    },
    "逻辑驱动性": {
        "positive": ["为什么", "原理", "因果", "理解", "底层"],
        "negative": ["套用", "步骤", "模板", "照做", "不知道"]
    },
    "实践验证性": {
        "positive": ["用", "实践", "做", "验证", "实验", "项目"],
        "negative": ["学完", "看懂", "理论上", "以后"]
    }
}


def analyze_text(text: str) -> Dict[str, Tuple[int, List[str]]]:
    """分析文本，返回各维度得分和匹配关键词"""
    text = text.lower()
    results = {}

    for dimension, pattern in PATTERNS.items():
        pos_matches = [w for w in pattern["positive"] if w in text]
        neg_matches = [w for w in pattern["negative"] if w in text]

        if neg_matches:
            score = 0
        elif pos_matches:
            score = 2
        else:
            score = 1

        results[dimension] = (score, pos_matches + neg_matches)

    return results


def generate_diagnosis(analysis: Dict) -> List[str]:
    """生成问题诊断"""
    diagnosis = []

    for dim, (score, _) in analysis.items():
        if score == 0:
            for principle, positive, negative in PRINCIPLE_CHAIN:
                if dim in principle or principle in dim:
                    diagnosis.append(f"- {dim}: 处于{negative}模式，而非{positive}")
                    break

    return diagnosis


def generate_actions(analysis: Dict) -> List[str]:
    """生成改进建议"""
    actions = []

    dimension_actions = {
        "自学驱动性": "设定一个自主的学习目标，而非跟随外部课程表",
        "归纳总结性": "学完后花10分钟提炼3个核心要点，而非继续刷题",
        "自我输出性": "尝试用自己的话复述，而非摘抄教材原文",
        "表达重构性": "用一个类比或故事重新解释这个概念",
        "逻辑驱动性": "问自己三个为什么，追溯到底层原理",
        "实践验证性": "设计一个最小实验，用实践验证理解"
    }

    for dim, (score, _) in analysis.items():
        if score < 2:
            actions.append(f"{dim}改进: {dimension_actions.get(dim, '反思当前方法')}")

    return actions[:3]  # 最多3个行动


def calculate_efficiency(analysis: Dict, time_hours: float) -> Dict:
    """评估效率"""
    total = sum(score for score, _ in analysis.values())
    max_score = len(analysis) * 2

    if total <= 4:
        current_roi = "低"
        improved_roi = "高"
        reason = "被动学习模式，遗忘率高，迁移性差"
    elif total <= 8:
        current_roi = "中"
        improved_roi = "高"
        reason = "有意识但未内化，输出和重构不足"
    else:
        current_roi = "高"
        improved_roi = "高"
        reason = "第一性原理驱动，持续实践验证"

    return {
        "current_score": f"{total}/{max_score}",
        "current_roi": current_roi,
        "improved_roi": improved_roi,
        "reason": reason,
        "time_recommendation": f"当前{time_hours}小时/周，建议: {time_hours * 0.7:.1f}小时学习 + {time_hours * 0.3:.1f}小时输出实践"
    }


def analyze_learning(input_data: str) -> str:
    """主分析函数"""
    # 尝试解析JSON
    try:
        data = json.loads(input_data)
        text = f"{data.get('学习内容', '')} {data.get('当前方法', '')} {data.get('困惑', '')}"
        time_hours = float(data.get('时间投入', 1))
    except json.JSONDecodeError:
        # 直接分析文本
        text = input_data
        time_hours = 1

    # 分析
    analysis = analyze_text(text)
    diagnosis = generate_diagnosis(analysis)
    actions = generate_actions(analysis)
    efficiency = calculate_efficiency(analysis, time_hours)

    # 构建输出
    output = []
    output.append("## 学习第一性原理分析报告\n")

    output.append("### 1. 现状诊断")
    if diagnosis:
        output.extend(diagnosis)
    else:
        output.append("- 未发现明显违背第一性原理的模式")

    output.append("\n### 2. 改进建议")
    for i, action in enumerate(actions, 1):
        output.append(f"{i}. {action}")

    output.append("\n### 3. 效率评估")
    output.append(f"- 当前得分: {efficiency['current_score']}")
    output.append(f"- 当前ROI: {efficiency['current_roi']}")
    output.append(f"- 优化后ROI: {efficiency['improved_roi']}")
    output.append(f"- 原因: {efficiency['reason']}")
    output.append(f"- 调整建议: {efficiency['time_recommendation']}")

    output.append("\n### 4. 原理链对照")
    for dim, (score, _) in analysis.items():
        for principle, positive, negative in PRINCIPLE_CHAIN:
            if dim in principle or principle in dim:
                status = "✓" if score == 2 else ("△" if score == 1 else "✗")
                output.append(f"{status} {principle}: {positive if score >= 1 else negative}")
                break

    return "\n".join(output)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        result = analyze_learning(sys.argv[1])
        print(result)
    else:
        print("Usage: python analyze.py '<学习描述>'")
        print("Or: python analyze.py '<json数据>'")
