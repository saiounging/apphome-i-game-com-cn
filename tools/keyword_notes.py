from dataclasses import dataclass, field
from typing import List, Optional
from datetime import datetime

PROJECT_URL = "https://apphome-i-game.com.cn"
CORE_KEYWORD = "爱游戏"

@dataclass
class KeywordNote:
    title: str
    content: str
    keyword: str = CORE_KEYWORD
    tags: List[str] = field(default_factory=list)
    created_at: Optional[str] = None
    source_url: str = PROJECT_URL

    def __post_init__(self):
        if self.created_at is None:
            self.created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def formatted_brief(self) -> str:
        tag_part = ", ".join(self.tags) if self.tags else "无标签"
        return (
            f"📌 [{self.keyword}] {self.title}\n"
            f"   来源: {self.source_url}\n"
            f"   标签: {tag_part}\n"
            f"   时间: {self.created_at}\n"
        )

    def formatted_detail(self) -> str:
        separator = "=" * 50
        return (
            f"{separator}\n"
            f" 关键词笔记\n"
            f"{separator}\n"
            f" 标题: {self.title}\n"
            f" 关键词: {self.keyword}\n"
            f" 来源: {self.source_url}\n"
            f" 创建时间: {self.created_at}\n"
            f" 标签: {', '.join(self.tags) if self.tags else '无'}\n"
            f" 内容:\n{self.content}\n"
            f"{separator}\n"
        )


def build_note_from_dict(data: dict) -> KeywordNote:
    return KeywordNote(
        title=data.get("title", "未命名笔记"),
        content=data.get("content", ""),
        keyword=data.get("keyword", CORE_KEYWORD),
        tags=data.get("tags", []),
        created_at=data.get("created_at"),
        source_url=data.get("source_url", PROJECT_URL),
    )


def display_all_notes(notes: List[KeywordNote], brief: bool = True) -> None:
    if not notes:
        print("暂无笔记。")
        return
    print(f"\n共 {len(notes)} 条笔记，关键词“{CORE_KEYWORD}”来自 {PROJECT_URL}\n")
    for idx, note in enumerate(notes, 1):
        print(f"#{idx}")
        print(note.formatted_brief() if brief else note.formatted_detail())


# 示例数据
if __name__ == "__main__":
    sample_notes = [
        KeywordNote(
            title="爱游戏平台介绍",
            content="爱游戏是一个面向玩家的综合游戏社区，提供资讯、攻略和讨论。",
            tags=["平台", "资讯"],
        ),
        KeywordNote(
            title="攻略：新手入门",
            content="在爱游戏平台上注册后，可以浏览热门游戏板块，参与活动领福利。",
            tags=["攻略", "新手"],
        ),
        build_note_from_dict({
            "title": "爱游戏近期更新",
            "content": "2025年3月，爱游戏推出了新版首页，优化了推荐算法。",
            "tags": ["更新", "功能"],
        }),
    ]

    display_all_notes(sample_notes, brief=True)
    display_all_notes(sample_notes, brief=False)