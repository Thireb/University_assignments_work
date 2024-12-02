import tomotopy as tp

coh = tp.coherence.Coherence(mdl, coherence='u_mass')
average_coherence = coh.get_score()
print('Average:', average_coherence)
print()
