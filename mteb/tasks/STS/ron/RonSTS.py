from __future__ import annotations

from mteb.abstasks.TaskMetadata import TaskMetadata

from ....abstasks.AbsTaskSTS import AbsTaskSTS


class RonSTS(AbsTaskSTS):
    metadata = TaskMetadata(
        name="RonSTS",
        dataset={
            "path": "dumitrescustefan/ro_sts",
            "revision": "41a33183b739070f3d46d9d446492c1d2f98ce1a",
            "trust_remote_code": True,
        },
        description="High-quality Romanian translation of STSBenchmark.",
        reference="https://openreview.net/forum?id=JH61CD7afTv",
        type="STS",
        category="s2s",
        modalities=["text"],
        eval_splits=["test"],
        eval_langs=["ron-Latn"],
        main_score="cosine_spearman",
        date=("2020-01-01", "2021-01-31"),
        domains=["News", "Social", "Web", "Written"],  # web for image captions
        task_subtypes=None,
        license="cc-by-4.0",  # not specified
        annotations_creators="human-annotated",
        dialect=[],
        sample_creation="machine-translated and verified",
        bibtex_citation=r"""
@inproceedings{dumitrescu2021liro,
  author = {Dumitrescu, Stefan Daniel and Rebeja, Petru and Lorincz, Beata and Gaman, Mihaela and Avram, Andrei and Ilie, Mihai and Pruteanu, Andrei and Stan, Adriana and Rosia, Lorena and Iacobescu, Cristina and others},
  booktitle = {Thirty-fifth Conference on Neural Information Processing Systems Datasets and Benchmarks Track (Round 1)},
  title = {LiRo: Benchmark and leaderboard for Romanian language tasks},
  year = {2021},
}
""",
    )

    @property
    def metadata_dict(self) -> dict[str, str]:
        metadata_dict = super().metadata_dict
        metadata_dict["min_score"] = 0
        metadata_dict["max_score"] = 5
        return metadata_dict
