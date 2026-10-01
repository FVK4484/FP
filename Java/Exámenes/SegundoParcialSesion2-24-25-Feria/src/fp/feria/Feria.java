package fp.feria;
import java.util.HashSet;
import java.util.Objects;
import java.util.Set;

public class Feria {
	
	private Integer anyo;
	private Set<CasetaFeria> casetas;
	
	public Feria(Set<CasetaFeria> casetas) {
		super();
		this.casetas = new HashSet<>(casetas);
	}
	

	public Integer getAnyo() {
		return anyo;
	}



	public Set<CasetaFeria> getCasetas() {
		return casetas;
	}


	public String toString() {
		return "Feria [anyo=" + anyo + ", casetas=" + casetas.size() + "]";
	}


	public int hashCode() {
		return Objects.hash(anyo, casetas);
	}


	public boolean equals(Object obj) {
		if (this == obj)
			return true;
		if (obj == null)
			return false;
		if (getClass() != obj.getClass())
			return false;
		Feria other = (Feria) obj;
		return Objects.equals(anyo, other.anyo) && Objects.equals(casetas, other.casetas);
	}
	
	public Integer getNumeroCasetas() {
		return casetas.size();
	}
	
	public void incorporarCaseta(CasetaFeria caseta) {
		casetas.add(caseta);
	}
	
	public void eliminaCaseta(CasetaFeria caseta) {
		casetas.remove(caseta);
	}
	
}
