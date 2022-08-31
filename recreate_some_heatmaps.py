# %%
import calour as ca
import os
#import rpy2
import re
os.chdir("/pita/users/rotem/MGV")
# %%
exp = ca.read_qiime2("table.qza", "project.tsv", normalize = 1e4, min_reads = 2e3)
exp = exp.filter_by_metadata("Cohort", ["MGV"])
exp = exp.cluster_features(10)
exp
# %%
exp = exp.sort_by_metadata("pnid")
exp = exp.sort_by_metadata("time")
exp = exp.sort_by_metadata("gel")
exp = exp.sort_by_metadata("pnid")
exp.sample_metadata.pnid = exp.sample_metadata.pnid.str.replace("MGV","")
exp.sample_metadata["Database"] = exp.sample_metadata._sample_id.str[2:4]
pl = exp.plot(barx_fields = ["gel","time", "pnid"], gui = "cli")
pl.save_figure("figure.png")
# %%
exp = exp.sort_by_metadata("clustered")
pl = exp.plot(barx_fields = ["clustered", "pnid", "time"], gui = "cli")
pl.save_figure("cluster.png")
# %%
exp = exp.sort_by_metadata("gel")
pl = exp.plot(barx_fields = ["gel","time", "pnid"], gui = "cli")
pl.save_figure("fig1.png")

# %%
exp = exp.sort_by_metadata("Database")
exp = exp.sort_by_metadata("pnid")
pl = exp.plot(barx_fields = ["Database", "pnid"], gui = "cli")
pl.save_figure("fig2.png")

# %%
dif = exp.diff_abundance(field = "gel", val1 = ["G", "N"],val2 = "h", random_seed = int(5782), alpha = .5)
dif = dif.sort_by_metadata("gel")
pl = dif.plot(barx_fields = ["gel","time", "pnid"], gui = "cli")
pl.save_figure("fig3.png")
