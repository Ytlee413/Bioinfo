idr <- "SLENSSNKNEKEKSAPSRTKQTENASQAKQLAELLRLSGPVMQQSQQPQPLQKQPPQPQQQQRPQQQQPHHPQTESVNSYSASGSTNPYMRRPNPVSPYPNSSHTSDIYGSTSPMNFYSTSSQAAGSYLNSSNPMNPYPGLLNQNTQYPSYQCNGNLSVDNCSPYLGSYSPQSQPMDLYRYPSQDPLSKLSLPPIHTLYQPRFGNSQSFTSKYLGYGNQNMQGDGFSSCTIRPNVHHVGKLPPYPTHEMDGHFMGATSRLPPNLSNPNMDYKNGEHHSPSHIIHNYSAAPGMFNSSLHALHLQNKENDMLSHTANGLSKMLPALNHDRTACVQGGLHKLSDANGQEKQPLALVQGVASGAEDN"
pep <- strsplit(idr, "")[[1]]
pep

aa_group <- "GAVCPLIMWFSTYNQKRHDE"
aa_group <- strsplit(aa_group, "")[[1]]
aa_group

#use aa_group and pep as input
positions = c()
for (a in 1: length(aa_group)) {
  for (p in 1:length(pep)) {
    if (aa_group[a] == pep[p]) {
      positions <- rbind(c(aa_group[a], p,a), positions)
    }
  }
}
pos <- positions[,-1]
rownames(pos) <- positions[,1]
options(repr.plot.width = 10, repr.plot.height = 6)
plot(pos, pch = 20, yaxt="n")
axis(2, at=pos[,2], labels=rownames(pos), las=2)