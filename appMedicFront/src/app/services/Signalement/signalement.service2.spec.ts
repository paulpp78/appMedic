import { TestBed, inject } from '@angular/core/testing';
import { HttpClientTestingModule, HttpTestingController } from '@angular/common/http/testing';
import { SignalementService } from './signalement.service';
import { HttpClientModule } from '@angular/common/http';
import { Signalement } from '../../models/signalement';

describe('SignalementService', () => {
  let service: SignalementService;
  let httpMock: HttpTestingController;

  beforeEach(() => {
    TestBed.configureTestingModule({
      imports: [HttpClientTestingModule, HttpClientModule],
      providers: [SignalementService]
    });
    service = TestBed.inject(SignalementService);
    httpMock = TestBed.inject(HttpTestingController);
  });

  afterEach(() => {
    httpMock.verify();
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });

  it('should update signalement', () => {
    const mockSignalement: Signalement = { id: '1', pseudo: 'testPseudo', code_cip: 'testCodeCIP' };
    const modifiedCount = 1;

    service.updateSignalement(mockSignalement).subscribe(response => {
      expect(response).toBeDefined();
      expect(response.message).toEqual('Signalement mis à jour');
      expect(response.modified_count).toEqual(modifiedCount);
    });

    const request = httpMock.expectOne('/api/signalement/1');
    expect(request.request.method).toBe('PUT');
    request.flush({ message: 'Signalement mis à jour', modified_count: modifiedCount });
  });
});
